from random import randint
from model.status.Status import Status
from model.Pokemon import Pokemon

class SpdDropEffect():

    def __init__(self, probability : int, forUser : bool = False):
        self.probability = probability
        self.forUser = forUser

    def getForUser(self)->bool:
        """
        Indicate if the effect must be applied to the user of the move (or else to the opponent)
        @return forUser attribute
        """
        return self.forUser


    def applyEffect(self, pokemon : Pokemon)->bool:
        """
        apply this effect to the pokemon
        @param the pokemon to apply the effect
        @return if the effect has been applied
        """
        if(randint(0,100)<=self.probability):
            pokemon.decreaseSpd()
            return True
        return False


    def getEffectMessage(self):
        return "Defense Spéciale baisse !"