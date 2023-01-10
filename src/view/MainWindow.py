from time import sleep
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from view.SelectPopup import SelectPopup

from view.PokemonLayout import PokemonLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        mainLayout = QGridLayout()

        self.opponentPokemon = PokemonLayout()
        self.allyPokemon = PokemonLayout()

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
        
        self.movesButtons = [self.move_button_1, self.move_button_2]
        movesFunctions = [self.onclick_moveButton_1, self.onclick_moveButton_2]
        
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
        playButton.clicked.connect(self.onClick_playButton)
        playButton.setMinimumSize(150,50)
        mainLayout.addWidget(playButton,1,0) 

        #Status Bar
        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar,1,1)

        self.setLayout(mainLayout)

    
    def resetGame(self):
        
        for b in self.movesButtons:
            b.setText("")
            b.setEnabled(False)

        for b in self.switchButtons:
            b.setText("")
            b.setEnabled(False)

        self.allyPokemon.withdrawPokemon()
        self.opponentPokemon.withdrawPokemon()

    def setController(self, controller):
        self.controller = controller   

    def displayText(self,msg) : 
        self.statusBar.showMessage(msg)

    def pause(self, secondes):
        for s in range(secondes):
            QCoreApplication.processEvents()
            sleep(1)  

    def onClick_playButton(self):
        self.controller.newGame()
    
    def selectTeam(self, namesList, forPlayer1):

        statusBar = QStatusBar()
        if forPlayer1 : 
            statusBar.showMessage("Selectionner vos Pokemon")
        else : 
            statusBar.showMessage("Selectionner les Pokemon adverses")

        combo_1 = QComboBox()
        combo_2 = QComboBox()
        combo_3 = QComboBox()

        combo_1.addItems(namesList)
        combo_2.addItems(namesList)
        combo_3.addItems(namesList)

        popup = SelectPopup(statusBar, combo_1, combo_2, combo_3)

        selectedNames = [
            combo_1.currentText(),
            combo_2.currentText(),
            combo_3.currentText()
        ]

        return selectedNames
        
    def setAllyPokemon(self, pokemon):
        self.displayText("{}, go !".format(pokemon.getName()))
        self.pause(1)
        self.allyPokemon.setPokemon(pokemon, True)
        self.pause(2)
        self.displayText("")

    def setOpponentPokemon(self, pokemon):
        self.displayText("L'adversaire envoie {}.".format(pokemon.getName()))
        self.pause(1)
        self.opponentPokemon.setPokemon(pokemon, False)
        self.pause(2)
        self.displayText("")

    def withdrawAllyPokemon(self):
        self.displayText("{}, reviens !".format(self.allyPokemon.getPokemonName()))
        self.pause(1)
        self.allyPokemon.withdrawPokemon()
        self.pause(1)
        self.displayText("")


    def waitForAction(self, trainer):

        self.displayText("Que dois faire {} ?".format(trainer.getCurrentPokemon().getName()))

        self.currentTrainer = trainer

        #Set moves
        self.move_button_1.setText(trainer.getCurrentPokemon().move1.getName())
        self.move_button_2.setText(trainer.getCurrentPokemon().move2.getName())
        self.move_button_1.setEnabled(True)
        self.move_button_2.setEnabled(True)
        
        #Set team
        self.switch_button_1.setText(trainer.getTeam()[0].getName())
        self.switch_button_2.setText(trainer.getTeam()[1].getName())
        self.switch_button_1.setEnabled(True)
        self.switch_button_2.setEnabled(True)

        self.waitingAction = True
        while self.waitingAction :
            qApp.processEvents()

    def sendAction(self, command):
        self.waitingAction = False
        self.move_button_1.setEnabled(False)
        self.move_button_2.setEnabled(False)
        self.switch_button_1.setEnabled(False)
        self.switch_button_2.setEnabled(False)
        self.currentTrainer.setActionCommand(command)

    def onclick_moveButton_1(self):
        self.sendAction("move_1")

    def onclick_moveButton_2(self):
        self.sendAction("move_2")

    def onclick_switchButton_1(self):
        self.sendAction("switch_1")

    def onclick_switchButton_2(self):
        self.sendAction("switch_2")

    def playMove_success(self, user, move, target, damage):
        self.displayText("{} utilise {} !".format(user.getName(), move.getName()))
        self.pause(1)
        self.allyPokemon.refreshHP()
        self.opponentPokemon.refreshHP()
        self.displayText("{} perd {} PV.".format(target.getName(), damage))
        self.pause(2)
        if(self.opponentPokemon.getPokemon().getPourcentageHP() == 0):
            self.displayText("{} est K.O. !!".format(self.opponentPokemon.getPokemon().getName(), damage))
            self.pause(2)
            self.opponentPokemon.withdrawPokemon()
        if(self.allyPokemon.getPokemon().getPourcentageHP() == 0):
            self.displayText("{} est K.O. !!".format(self.allyPokemon.getPokemon().getName(), damage))
            self.pause(2)
            self.allyPokemon.withdrawPokemon()
        self.displayText("")

    def playMove_miss(self, user, move, target):
        self.displayText("{} utilise {} !".format(user.getName(), move.getName()))
        self.pause(2)
        self.displayText("{} évite l'attaque...".format(target.getName()))
        self.pause(1)
        self.displayText("")