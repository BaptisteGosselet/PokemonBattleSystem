from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from model.Pokemon import Pokemon

class PokemonLayout(QVBoxLayout):

    def __init__(self, isAlly : bool, view):
        """
        Pokemon layout's constructor
        @param : 
            - isAlly, a boolean in order to know if the pokemon must be displayed from front or behind
            - view, the view to be able to display text
        """
        super().__init__()

        self.view = view
        self.pokemon = None

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

        self.isAlly = isAlly

    def getPokemon(self) -> Pokemon :
        """
        A getter for the current Pokemon
        """
        return self.pokemon

    def setPokemon(self, pokemon : Pokemon) -> None:
        """
        Set the Pokemon and display it on the screen (sprites, and datas)
        @param : pokemon, the pokemon to display
        """

        if(pokemon.getTrainer().getIsAI()) : 
            self.view.displayText("{} envoie {}.".format(pokemon.getTrainer().getName(),pokemon.getName()))
        else:
            self.view.displayText("{}, go !".format(pokemon.getName()))
        
        #Set pokemon
        self.pokemon = pokemon

        #Set name
        self.name.setText(pokemon.getName())

        #Set health_bar
        self.health_bar.setValue(pokemon.getPourcentageHP())
        self.health_bar.setVisible(True)

        #Set the sprite
        pix = QPixmap(self.getCurrentPokemonSpriteFilename())
        if pix.isNull() : 
            pix = QPixmap("img/sprites/missing.png")
        pix = pix.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.sprite.setPixmap(pix)

        self.view.displayText()

    def setPokemon_noMessage(self, pokemon : Pokemon) -> None:
        """
        setPokemon method without message
        @param : pokemon, the pokemon to display
        """

        self.pokemon = pokemon
        self.name.setText(pokemon.getName())
        self.health_bar.setValue(pokemon.getPourcentageHP())
        self.health_bar.setVisible(True)

        #Set the sprite
        pix = QPixmap(self.getCurrentPokemonSpriteFilename())
        if pix.isNull() : 
            pix = QPixmap("img/sprites/missing.png")
        pix = pix.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.sprite.setPixmap(pix)

    def withdrawPokemon(self) -> None :
        """
        Withdraw the displayed pokemon from the screen (and unset it)
        """
        if(self.pokemon != None) : 
            if(self.pokemon.getTrainer().getIsAI()) : 
                self.view.displayText("{} est retiré par Dresseur {}.".format(self.pokemon.getName(), self.pokemon.getTrainer().getName()))
            else :
                self.view.displayText("{}, reviens !".format(self.pokemon.getName()))
            self.withdrawPokemon_noMessage()

    def withdrawPokemon_noMessage(self) -> None :
        """
        Withdraw the displayed pokemon from the screen (and unset it)
        """
        if(self.pokemon != None) : 
            self.pokemon = None
            self.name.setText("")
            self.health_bar.setVisible(False)
            self.sprite.setPixmap(QPixmap())
            self.view.displayText()

    def getCurrentPokemonSpriteFilename(self) -> str:
        """
        return the filename of the sprite to display
        Ressources : 
            - https://archives.bulbagarden.net/wiki/Category:Red_and_Blue_sprites
            - https://archives.bulbagarden.net/wiki/Category:Generation_I_back_sprites
        """
        sprite_filename = "img/sprites/"
        sprite_filename += "back/" if (self.isAlly) else "front/"
        sprite_filename += self.pokemon.getName().lower()
        sprite_filename += ".png"
        return sprite_filename

    #TODO Status
    def refresh(self) -> None:
        """
        Refresh pokemon's datas such as his HP or status
        """
        self.health_bar.setValue(self.pokemon.getPourcentageHP())

