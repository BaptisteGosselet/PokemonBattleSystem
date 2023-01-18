from random import randint
from model.Pokemon import Pokemon

class StatusEffect():
     
    def __init__(self, probability):
        self.probability = probability

    def applyEffect(self, pokemon : Pokemon):
        """
        Apply an effect to the pokemon according to the probability
        Set the pokemon itself or a decorator of the pokemon with the status
        @param pokemon
        @return bool if it worked
        """
        if(randint(0,100) <= self.probability):
            return pokemon.setStatus(self.getStatusPokemon(pokemon))
        return False

    def getStatusPokemon(self, pokemon):
        """
        @param pokemon
        @return a decorator of the pokemon to apply the status
        """
        return Pokemon(
            pokemon.getName(), pokemon.getType1(), pokemon.getType2(),
            pokemon.getMaxHPStat(), pokemon.getAtkStat(), pokemon.getDefStat(),
            pokemon.getSpaStat(), pokemon.getSpdStat(), pokemon.getSpeStat(), 
            pokemon.getMove1(), pokemon.getMove2()
        )

