from time import sleep
from PyQt5.QtCore import QCoreApplication
from PyQt5 import Qt
from PyQt5.QtWidgets import *
from model.PokemonFactory import PokemonFactory
from model.trainer.AITrainer import AITrainer
from view.TrainerGeneratorPopup import TrainerGeneratorPopup

from controller.BattleController import BattleController
from model.trainer.Trainer import Trainer
from model.Pokemon import Pokemon
from controller.action.MoveAction import MoveAction

from view.PokemonLayout import PokemonLayout


class MainWindow(QWidget):

    def __init__(self) -> None :
        super().__init__()
        mainLayout = QGridLayout()

        #Status Bar
        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar,1,1)

        #Pokemon's layout
        self.opponentPokemon = PokemonLayout(False, self)
        self.allyPokemon = PokemonLayout(True, self)

        #Battle screen
        battleScreen = QGridLayout()
        battleScreen.addItem(QSpacerItem(200, 100),1,0)
        battleScreen.addLayout(self.opponentPokemon,0,2)
        battleScreen.addLayout(self.allyPokemon,1,0)
        mainLayout.addLayout(battleScreen,0,1)

        #Moves buttons layout
        movesGrid = QGridLayout()
        self.move_button_1 = QPushButton()
        self.move_button_2 = QPushButton()
        self.move_button_3 = QPushButton()
        self.move_button_4 = QPushButton()
        
        self.movesButtons = [self.move_button_1, self.move_button_2, self.move_button_3, self.move_button_4]
        movesFunctions = [self.onclick_moveButton_1, self.onclick_moveButton_2, self.onclick_moveButton_3, self.onclick_moveButton_4]
        
        for i in range(len(self.movesButtons)):
            self.movesButtons[i].setEnabled(False)
            self.movesButtons[i].setMinimumSize(150,50)
            self.movesButtons[i].clicked.connect(movesFunctions[i])
            movesGrid.addWidget(self.movesButtons[i],0+i,1)
        
        movesGrid.addItem(QSpacerItem(20,0),0,0)
        movesGrid.addItem(QSpacerItem(50,0),0,2+len(self.movesButtons))
        
        mainLayout.addLayout(movesGrid,0,0)

        #Switch buttons layout
        switchLayout = QGridLayout()
        self.switch_button_1 = QPushButton()
        self.switch_button_2 = QPushButton()

        self.switchButtons = [self.switch_button_1, self.switch_button_2]
        switchFunctions = [self.onclick_switchButton_1, self.onclick_switchButton_2]

        for i in range(len(self.switchButtons)):
            self.switchButtons[i].setEnabled(False)
            self.switchButtons[i].setMinimumSize(150,30)
            self.switchButtons[i].clicked.connect(switchFunctions[i])
            switchLayout.addWidget(self.switchButtons[i],0+i,1)
        
        switchLayout.addItem(QSpacerItem(50,0),0,0)
        switchLayout.addItem(QSpacerItem(20,0),0,2)

        mainLayout.addLayout(switchLayout,0,2)

        #Play Button
        playButton = QPushButton("Nouvelle Partie")
        playButton.clicked.connect(self.onClick_newGameButton)
        playButton.setMinimumSize(150,50)
        mainLayout.addWidget(playButton,1,0) 

        self.setLayout(mainLayout)

    def resetGame(self) -> None :
        """
        Reset game's element such as buttons and displayed pokemons
        """
    
        self.statusBar.showMessage("")

        for b in self.movesButtons:
            b.setText("")
            b.setEnabled(False)

        for b in self.switchButtons:
            b.setText("")
            b.setEnabled(False)

        self.allyPokemon.withdrawPokemon()
        self.opponentPokemon.withdrawPokemon()

    def setController(self, controller : BattleController) -> None :
        """
        Controller's setter
        @param : controller : BattleController
        """
        self.controller = controller   

    def displayText(self, msg : str = "", seconds : int = 1) -> None : 
        self.statusBar.showMessage(msg)
        for s in range(seconds):
            QCoreApplication.processEvents()
            sleep(1) 
        self.statusBar.showMessage("")

    def onClick_newGameButton(self) -> None:
        self.controller.newGame()
    
    def generateTrainers(self, pkmFactory : PokemonFactory) -> list[Trainer]:
        """
        Display a popup window in order to generate the two trainers of the game, their name and their pokemon
        @param : pkmFactory, the class allowing pokemon's generation
        """

        namesList = pkmFactory.getNamesList()

        #Initialisation des champs de la fenêtre
        combos_J1 = [QComboBox(), QComboBox(), QComboBox()]
        combos_J2 = [QComboBox(), QComboBox(), QComboBox()]

        for combo in combos_J1 : 
            combo.addItems(namesList)
        
        for combo in combos_J2 : 
            combo.addItems(namesList)

        saisieNom_J1 = QTextEdit("Joueur 1")
        saisieNom_J2 = QTextEdit("Joueur 2")
        caseAI = QCheckBox("J2 ORDI")
        caseAI.setChecked(True)


        popup = TrainerGeneratorPopup(saisieNom_J1, saisieNom_J2, caseAI, combos_J1, combos_J2)

        trainer_1 = Trainer(saisieNom_J1.toPlainText(), [
                    pkmFactory.generatePokemon(combos_J1[0].currentText()), 
                    pkmFactory.generatePokemon(combos_J1[1].currentText()), 
                    pkmFactory.generatePokemon(combos_J1[2].currentText()), 
                ], self.allyPokemon)        
                
        if(caseAI.isChecked()):
            trainer_2 = AITrainer(saisieNom_J2.toPlainText(), [
                        pkmFactory.generatePokemon(combos_J2[0].currentText()), 
                        pkmFactory.generatePokemon(combos_J2[1].currentText()), 
                        pkmFactory.generatePokemon(combos_J2[2].currentText()), 
                    ], self.opponentPokemon)
        else : 
            trainer_2 = Trainer(saisieNom_J2.toPlainText(), [
                        pkmFactory.generatePokemon(combos_J2[0].currentText()), 
                        pkmFactory.generatePokemon(combos_J2[1].currentText()), 
                        pkmFactory.generatePokemon(combos_J2[2].currentText()), 
                    ], self.opponentPokemon)

        return [trainer_1, trainer_2]

    def waitForAction(self, trainer : Trainer) -> None :
        """
        Pause the program until the player choose an action
        @param : trainer, the player who must play
        """

        self.currentTrainer = trainer

        if(not trainer.getCurrentPokemon().getIsKo()):
            self.statusBar.showMessage("Que dois faire {} ?".format(trainer.getCurrentPokemon().getName()))

            #Set moves
            self.move_button_1.setText(trainer.getCurrentPokemon().getMove1().getName())
            self.move_button_1.setToolTip(trainer.getCurrentPokemon().getMove1().getDescriptionText())

            self.move_button_2.setText(trainer.getCurrentPokemon().getMove2().getName())
            self.move_button_2.setToolTip(trainer.getCurrentPokemon().getMove2().getDescriptionText())

            self.move_button_3.setText(trainer.getCurrentPokemon().getMove3().getName())
            self.move_button_3.setToolTip(trainer.getCurrentPokemon().getMove3().getDescriptionText())

            self.move_button_4.setText(trainer.getCurrentPokemon().getMove4().getName())
            self.move_button_4.setToolTip(trainer.getCurrentPokemon().getMove4().getDescriptionText())

            self.move_button_1.setEnabled(True)
            self.move_button_2.setEnabled(True)
            self.move_button_3.setEnabled(True)
            self.move_button_4.setEnabled(True)
        
        #Set team
        self.switch_button_1.setText(trainer.getTeam()[0].getName())
        if(not trainer.getTeam()[0].getIsKo()):
            self.switch_button_1.setEnabled(True)   
        
        self.switch_button_2.setText(trainer.getTeam()[1].getName())
        if(not trainer.getTeam()[1].getIsKo()):
            self.switch_button_2.setEnabled(True)

        self.waitingAction = True
        while self.waitingAction :
            qApp.processEvents()

    def sendCommand(self, command : str) -> None :
        """
        A method receiving the command (such as move_1 or switch_1) from a button click, and send it to the playing trainer
        @param : command, a command to send
        """
        self.waitingAction = False
        self.move_button_1.setEnabled(False)
        self.move_button_2.setEnabled(False)
        self.move_button_3.setEnabled(False)
        self.move_button_4.setEnabled(False)
        self.switch_button_1.setEnabled(False)
        self.switch_button_2.setEnabled(False)
        self.currentTrainer.setActionCommand(command)

    def onclick_moveButton_1(self) -> None :
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("move_1")

    def onclick_moveButton_2(self) -> None :
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("move_2")

    def onclick_moveButton_3(self) -> None :
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("move_3")

    def onclick_moveButton_4(self) -> None :
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("move_4")

    def onclick_switchButton_1(self) -> None:
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("switch_1")

    def onclick_switchButton_2(self) -> None:
        """
        A method executed by a button press, it calls the sendCommand method with the corresponding parameter
        """
        self.sendCommand("switch_2")

    def playMove(self, action : MoveAction) -> None:
        """Show a action after its execution
        @param action, the action to show on the screen
        """
        if(type(action)==MoveAction):

            if(action.getFailByStatus()):
                self.displayText(action.getFailMessage(),2)
            else:

                self.displayText("{} utilise {} !".format(action.getMyPokemon().getName(), action.getMove().getName()))
                self.allyPokemon.refresh()
                self.opponentPokemon.refresh()

                if(action.getMissed()):
                    self.displayText("{} évite l'attaque...".format(action.getTarget().getName()), 2)
                else:    
                    if(action.getImmunite()):
                        self.displayText("Ça n'affecte pas.")
                    else:
                        if(action.getDamage()>0):
                            self.displayText("{} perd {} PV.".format(action.getTarget().getName(), action.getDamage()))

                            if(action.getCoupCritique()):
                                self.displayText("Coup Critique !")

                            if(action.getPeuEfficace()):
                                self.displayText("Ce n'est pas très efficace...")

                            elif(action.getSuperEfficace()):
                                self.displayText("C'est super efficace !")
                
                if(action.getEffectSetted()):
                    self.displayText(action.getEffectMessage(),1)                        

                if(self.opponentPokemon.getPokemon().getIsKo()):
                    self.displayText("{} est K.O. !!".format(self.opponentPokemon.getPokemon().getName(), action.getDamage()),3)
                    self.opponentPokemon.withdrawPokemon_noMessage()
                if(self.allyPokemon.getPokemon().getIsKo()):
                    self.displayText("{} est K.O. !!".format(self.allyPokemon.getPokemon().getName(), action.getDamage()),3)
                    self.allyPokemon.withdrawPokemon_noMessage()            

    def displayWinner(self, winner) -> None :
        """
        Display the winner's name at the end of the game
        """
        self.statusBar.showMessage("{} remporte le combat !".format(winner.getName()))