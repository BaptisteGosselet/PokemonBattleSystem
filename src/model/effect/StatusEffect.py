from random import randint
from model.status.Status import Status
from model.Pokemon import Pokemon

class SecondaryEffect():

    def __init__(self, status : Status, probability : int):
        self.status = status
        self.probability = probability

    def applyEffect(self, pokemon : Pokemon)->bool:
        """
        apply this effect to the pokemon
        @param the pokemon to apply the effect
        @return if the effect has been applied
        """
        if(randint(0,100)<=self.probability):
            if(pokemon.getStatus() == None):
                pokemon.setStatus(self.status)
                return True
            else:
                return False
        return False