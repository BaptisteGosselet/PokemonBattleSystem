from math import ceil
from model.Move import Move
from model.TypePkmn import TypePkmn
from model.status.ParalysisStatus import ParalysisStatus
from model.status.Status import Status


class Pokemon : 

    def __init__(self, name, type1, type2,  hp, atkStat, defStat, spaStat, spdStat, speStat, move1, move2):
    
        self.name = name 
        self.type1 = type1
        self.type2 = type2
        
        self.MAX_HP = 2*hp+100+10
        self.current_HP = self.MAX_HP
        self.atkStat = atkStat
        self.defStat = defStat
        self.spaStat = spaStat
        self.spdStat = spdStat
        self.speStat = speStat

        self.move1 = move1
        self.move2 = move2

        self.status = None

        self.trainer = None

        self.isKo = False


    def getName(self)->str:
        return self.name

    def getMove1(self)->Move:
        return self.move1

    def getMove2(self)->Move:
        return self.move2

    def getPourcentageHP(self)->int:
        return ceil((self.current_HP / self.MAX_HP) * 100)

    def getAtkStat(self)->int:
        return self.atkStat

    def getDefStat(self)->int:
        return self.defStat

    def getSpaStat(self)->int:
        return self.spaStat

    def getSpdStat(self)->int:
        return self.spdStat

    def getSpeStat(self)->int:
        if(type(self.status)==ParalysisStatus):
            return self.speStat // 4
        return self.speStat

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

    def applyDamage(self, damage)->None:
        """
        Apply a number of damage to the HP, if current HPs are lower to 0 then the pokemon is K.O.
        """
        self.current_HP -= damage
        if(self.current_HP < 0):
            self.current_HP = 0
            self.isKo = True