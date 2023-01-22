from random import randint
from model.Pokemon import Pokemon

class StatChangeEffect():

    def __init__(self, modifTab : list[int], prob : int, forUser : bool = False):
        self.modifTab = modifTab #[ATK, DEF, SPA, SPD, SPE]
        self.prob = prob
        self.forUser = forUser

    def getForUser(self)->bool:
        """
        Indicate if the effect must be applied to the user of the move (or else to the opponent)
        @return forUser attribute
        """
        return self.forUser


    def applyEffect(self, pokemon : Pokemon)->bool:
        if(randint(0,100) < self.prob):
            pokemon.modifAtk(self.modifTab[0])
            pokemon.modifDef(self.modifTab[1])
            pokemon.modifSpa(self.modifTab[2])
            pokemon.modifSpd(self.modifTab[3])
            pokemon.modifSpe(self.modifTab[4])
            return True
        return False

    def getEffectMessage(self):
        s1 = ""
        if(self.modifTab[0] > 0):
            s1 += "Attaque "
        if(self.modifTab[1] > 0):
            s1 += "Defense "
        if(self.modifTab[2] > 0):
            s1 += "Attaque Spéciale "
        if(self.modifTab[3] > 0):
            s1 += "Défense Spéciale "
        if(self.modifTab[4] > 0):
            s1 += "Vitesse "
        if(s1 != ""):
            s1 += "augmente !\n"

        s2 = ""
        if(self.modifTab[0] < 0):
            s2 += "Attaque "
        if(self.modifTab[1] < 0):
            s2 += "Defense "
        if(self.modifTab[2] < 0):
            s2 += "Attaque Spéciale "
        if(self.modifTab[3] < 0):
            s2 += "Défense Spéciale "
        if(self.modifTab[4] < 0):
            s2 += "Vitesse "
        if(s2 != ""):
            s2 += "baisse.\n"

        return s1 + s2