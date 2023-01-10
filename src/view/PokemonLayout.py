import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class PokemonLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()

        #Init name of the Pokemon
        self.name = QLabel()
        self.addWidget(self.name)

        #Health Bar
        self.health_bar = QProgressBar()
        self.health_bar.setRange(0,100)
        self.health_bar.setVisible(False)
        self.health_bar.setMaximumSize(150,100)
        self.addWidget(self.health_bar)

        #Sprite
        self.sprite = QLabel()
        self.sprite.setMinimumSize(150,150)
        self.addWidget(self.sprite)

    def setPokemon(self, pokemon, backSprite=False):
        
        #Set name
        self.name.setText(pokemon.getName())

        #Set health_bar
        self.health_bar.setValue(pokemon.getPourcentageHP())
        self.health_bar.setVisible(True)

        #Generate sprite's filename
        sprite_filename = "img/sprites/"
        sprite_filename += "back/" if (backSprite) else "front/"
        sprite_filename += pokemon.getName().lower()
        sprite_filename += ".png"

        #Set the sprite
        pix = QPixmap(sprite_filename)
        if pix.isNull() : 
            pix = QPixmap("img/sprites/missing.png")
        pix = pix.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.sprite.setPixmap(pix)

    def withdrawPokemon(self):
        self.name.setText("")
        self.health_bar.setVisible(False)
        self.sprite.setPixmap(QPixmap())

#Ressources : 
    #https://archives.bulbagarden.net/wiki/Category:Red_and_Blue_sprites
    #https://archives.bulbagarden.net/wiki/Category:Generation_I_back_sprites