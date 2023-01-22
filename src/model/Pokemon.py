from math import ceil
from model.Move import Move
from model.TypePkmn import TypePkmn
from model.status.BurnStatus import BurnStatus
from model.status.ParalysisStatus import ParalysisStatus
from model.status.Status import Status


class Pokemon : 

    def __init__(self, name, type1, type2,  hp, atkStat, defStat, spaStat, spdStat, speStat, move1, move2, move3, move4):
    
        self.name = name 
        self.type1 = type1
        self.type2 = type2
        
        self.MAX_HP = 2*hp+110
        self.current_HP = self.MAX_HP
        self.atkStat = atkStat
        self.defStat = defStat
        self.spaStat = spaStat
        self.spdStat = spdStat
        self.speStat = speStat

        self.atkModif = 0
        self.defModif = 0
        self.spaModif = 0
        self.spdModif = 0
        self.speModif = 0

        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

        self.status = None

        self.trainer = None

        self.isKo = False


    def getName(self)->str:
        return self.name

    def getMove1(self)->Move:
        return self.move1

    def getMove2(self)->Move:
        return self.move2

    def getMove3(self)->Move:
        return self.move3

    def getMove4(self)->Move:
        return self.move4

    def getPourcentageHP(self)->int:
        return ceil((self.current_HP / self.MAX_HP) * 100)

    def getMaxHP(self)->int:
        return self.MAX_HP

    def getAtkStat(self)->int:
        if(type(self.status)==BurnStatus):
            return int(self.atkStat // 2 + (self.atkModif*25/100))
        return int(self.atkStat + (self.atkModif*25/100))

    def getDefStat(self)->int:
        return int(self.defStat + (self.defModif*25/100))

    def getSpaStat(self)->int:
        return int(self.spaStat + (self.spaModif*25/100))

    def getSpdStat(self)->int:
        return int(self.spdStat + (self.spdModif*25/100))

    def getSpeStat(self)->int:
        if(type(self.status)==ParalysisStatus):
            return int(self.speStat // 4 + (self.speModif*25/100))
        return int(self.speStat + (self.speModif*25/100))

    def getIsKo(self)->bool:
        return self.isKo

    def getType1(self)->TypePkmn:
        return self.type1

    def getType2(self)->TypePkmn:
        return self.type2

    def setTrainer(self, trainer)->None:
        self.trainer = trainer

    def getTrainer(self):
        return self.trainer

    def setStatus(self, status):
        self.status = status

    def getStatus(self)->Status:
        return self.status

    def applyStatus(self):
        if(self.status != None):
            self.status.applyStatus(self)

    def increaseAtk(self):
        self.atkModif += 1  

    def decreaseAtk(self):
        self.atkModif -= 1

    def increaseDef(self):
        self.defModif += 1  

    def decreaseDef(self):
        self.defModif -= 1

    def increaseSpa(self):
        self.spaModif += 1  

    def decreaseSpa(self):
        self.spaModif -= 1

    def increaseSpd(self):
        self.spdModif += 1  

    def decreaseSpd(self):
        self.spdModif -= 1

    def increaseSpe(self):
        self.speModif += 1  

    def decreaseSpe(self):
        self.speModif -= 1

    def resetModif(self):
        self.atkModif = 0
        self.defModif = 0
        self.spaModif = 0
        self.spdModif = 0
        self.speModif = 0

    def heal(self, pv)->None:
        if(not self.isKo):
            self.current_HP += pv
            if(self.current_HP > self.MAX_HP):
                self.current_HP = self.MAX_HP

    def applyDamage(self, damage)->None:
        """
        Apply a number of damage to the HP, if current HPs are lower to 0 then the pokemon is K.O.
        """
        self.current_HP -= damage
        if(self.current_HP < 0):
            self.current_HP = 0
            self.isKo = True