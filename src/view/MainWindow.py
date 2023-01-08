import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from view.MovesLayout import MovesLayout
from view.PokemonLayout import PokemonLayout
from view.TeamLayout import TeamLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        mainLayout = QGridLayout()

        opponentPokemon = PokemonLayout()
        allyPokemon = PokemonLayout()

        #Battle screen
        battleScreen = QGridLayout()
        battleScreen.addItem(QSpacerItem(200, 100),1,0)
        battleScreen.addLayout(opponentPokemon,0,2)
        battleScreen.addLayout(allyPokemon,1,0)

        #Buttons layouts
        self.movesLayout = MovesLayout()
        self.teamLayout = TeamLayout()

        #Place all layouts
        mainLayout.addLayout(self.movesLayout,0,0)
        mainLayout.addLayout(battleScreen,0,1)
        mainLayout.addLayout(self.teamLayout,0,2)

        #Status Bar
        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar)

        self.setLayout(mainLayout)

    def showMessage(self,msg) : 
        self.statusBar.showMessage(msg)