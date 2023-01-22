from copy import deepcopy
from random import randint
from model.status.ParalysisStatus import ParalysisStatus
from model.status.PoisonStatus import PoisonStatus
from model.status.Status import Status
from model.Pokemon import Pokemon

class StatusEffect():

    def __init__(self, status : Status, probability : int, forUser : bool = False):
        self.status = status
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
            if(pokemon.getStatus() == None):

                if(type(self.status) == ParalysisStatus and pokemon.canParalyse()
                or type(self.status) == PoisonStatus and pokemon.canPoison()):
                    return False
                    
                pokemon.setStatus(deepcopy(self.status))
                return True
            
            
            else:
                return False
        return False

    def getEffectMessage(self):
        return self.status.getStatusMessage()