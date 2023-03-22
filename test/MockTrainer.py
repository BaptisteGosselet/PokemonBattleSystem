from testUtils import genererUnPokemon
from model.trainer.Trainer import Trainer
from MockView import MockView

class MockTrainer(Trainer):

    def __init__(self):
        super().__init__("Toto",
        [genererUnPokemon(), genererUnPokemon(), genererUnPokemon()],
        MockView())

    def setAllKO(self):
        self.currentPokemon.applyDamage(9999)
        for p in self.team:
            p.applyDamage(9999)

    def getView(self):
        return self.displayer
    
    def setArbitraryCurrentPokemon(self, pokemon):
        self.currentPokemon = pokemon
            