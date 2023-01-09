from model.Pokemon import Pokemon
from model.PokemonFactory import PokemonFactory
from model.Trainer import Trainer


class BattleController() : 

    def __init__(self):
        pass

    def setView(self, view):
        self.view = view

    def newGame(self):
        pkmFactory = PokemonFactory()


        dracaufeu = pkmFactory.generatePokemon("dracaufeu")
        leviator = pkmFactory.generatePokemon("leviator")
        grolem = pkmFactory.generatePokemon("grolem")
        alakazam = pkmFactory.generatePokemon("alakazam")
        ectoplasma = pkmFactory.generatePokemon("ectoplasma")
        tauros = pkmFactory.generatePokemon("tauros")


        t1 = Trainer("Joueur",[dracaufeu, leviator, grolem])
        t2 = Trainer("Ordinateur",[alakazam, ectoplasma, tauros])

        self.view.setOpponentPokemon(t2.getCurrentPokemon())

        self.view.setAllyPokemon(t1.getCurrentPokemon())
        
        self.play()

    def play(self):

        pass