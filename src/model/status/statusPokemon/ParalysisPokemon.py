from random import randint
from model.Pokemon import Pokemon

class ParalysisPokemon(Pokemon):

    def __init__(self, pokemon):
        super().__init__(pokemon.getName(), pokemon.getType1(), pokemon.getType2(),
            pokemon.getMaxHPStat(), pokemon.getAtkStat(), pokemon.getDefStat(),
            pokemon.getSpaStat(), pokemon.getSpdStat(), pokemon.getSpeStat(), 
            pokemon.getMove1(), pokemon.getMove2()
        )

        self.setCurrentHP(pokemon.getCurrentHP())
        self.pokemon = pokemon

    def setStatus(self, statusPokemon)->bool:
        return False
    
    def healStatus(self):
        print("healStatus")
        self.pokemon.setCurrentHP(self.getCurrentHP())
        self.trainer.setCurrentPokemon(self.pokemon)
        self = self.pokemon

    def canMove(self)->bool:
        return (randint(0,100)<=75)

    def getSpeStat(self) -> int:
        return super().getSpeStat() / 4
