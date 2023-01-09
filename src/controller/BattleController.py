from model.Pokemon import Pokemon
from model.Trainer import Trainer


class BattleController() : 

    def __init__(self):
        pass

    def setView(self, view):
        self.view = view

    def newGame(self):

        dracaufeu = Pokemon("Dracaufeu", 120)
        leviator = Pokemon("Leviator", 140)
        grolem = Pokemon("Grolem", 140)
        alakazam = Pokemon("Alakazam", 140)
        ectoplasma = Pokemon("Ectoplasma", 140)
        tauros = Pokemon("Tauros", 140)


        t1 = Trainer("Joueur",[dracaufeu, leviator, grolem])
        t2 = Trainer("Ordinateur",[alakazam, ectoplasma, tauros])

        self.view.setOpponentPokemon(t2.getCurrentPokemon())

        self.view.setAllyPokemon(t1.getCurrentPokemon())
        
        self.play()

    def play(self):

        pass