import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class PokemonLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()

        #name of pokemon
        name = QLabel('Dracaufeu')
        self.addWidget(name)

        #Health Bar
        health_bar = QProgressBar()
        health_bar.setRange(0,100)
        health_bar.setMaximumSize(150,100)
        self.addWidget(health_bar)

        #Sprite
        sprite = QLabel()
        pix = QPixmap("img/charizard.png")
        pix = pix.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        sprite.setPixmap(pix)
        self.addWidget(sprite)

