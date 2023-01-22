from random import randint
from model.Pokemon import Pokemon

class HealAndRecoilEffect():

    def __init__(self, pourcent_pv : int, forUser : bool = False):
        self.pourcent_pv = pourcent_pv
        self.forUser = forUser

    def getForUser(self)->bool:
        """
        Indicate if the effect must be applied to the user of the move (or else to the opponent)
        @return forUser attribute
        """
        return self.forUser


    def applyEffect(self, pokemon : Pokemon)->bool:
        pv_concrets = self.pourcent_pv * pokemon.getMaxHP() // 100
        if(pv_concrets >= 0):
            pokemon.heal(pv_concrets)
        else:
            pokemon.applyDamage(pv_concrets * -1)
        return True


    def getEffectMessage(self):
        if(self.pourcent_pv >= 0):
            return "Le Pokémon récupère des PV"
        else:
            return "Le Pokémon prends des dégats."