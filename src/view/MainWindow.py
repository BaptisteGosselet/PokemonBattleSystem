from time import sleep
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *

from view.MovesLayout import MovesLayout
from view.PokemonLayout import PokemonLayout
from view.TeamLayout import TeamLayout


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

        #Buttons layouts
        self.movesLayout = MovesLayout()
        self.teamLayout = TeamLayout()

        #Place all layouts
        mainLayout.addLayout(self.movesLayout,0,0)
        mainLayout.addLayout(battleScreen,0,1)
        mainLayout.addLayout(self.teamLayout,0,2)

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

    def onClick_playButton(self):
        self.controller.newGame()

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

    def pause(self, secondes):
        for s in range(secondes):
            QCoreApplication.processEvents()
            sleep(1)
            