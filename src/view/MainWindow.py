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
        movesGrid.addItem(QSpacerItem(20,0),0,0)
        
        self.move_button_1 = QPushButton()
        self.move_button_1.setEnabled(False)
        self.move_button_1.setMinimumSize(150,50)
        self.move_button_1.clicked.connect(self.onclick_moveButton_1)
        movesGrid.addWidget(self.move_button_1,0,1)

        self.move_button_2 = QPushButton()
        self.move_button_2.setEnabled(False)
        self.move_button_2.setMinimumSize(150,50)
        self.move_button_2.clicked.connect(self.onclick_moveButton_2)
        movesGrid.addWidget(self.move_button_2,1,1)
        movesGrid.addItem(QSpacerItem(50,0),0,2)

        mainLayout.addLayout(movesGrid,0,0)

        #Switch buttons layout
        switchLayout = QGridLayout()
        switchLayout.addItem(QSpacerItem(50,0),0,0)


        self.switch_button_1 = QPushButton()
        self.switch_button_1.setEnabled(False)
        self.switch_button_1.setMinimumSize(150,30)
        self.switch_button_1.clicked.connect(self.onclick_switchButton_1)
        switchLayout.addWidget(self.switch_button_1,0,1)
        

        self.switch_button_2 = QPushButton()
        self.switch_button_2.setEnabled(False)
        self.switch_button_2.setMinimumSize(150,30)
        self.switch_button_2.clicked.connect(self.onclick_switchButton_2)
        switchLayout.addWidget(self.switch_button_2,1,1)
                
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

    def withdrawAllyPokemon(self, pokemon):
        self.displayText("{}, reviens !".format(pokemon.getName()))
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



