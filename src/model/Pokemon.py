from model.TypePkmn import TypePkmn


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


        self.trainer = None
        self.isKo = False


    def getName(self)->str:
        return self.name

    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getCurrentHP(self):
        return self.current_HP

    def setCurrentHP(self, n):
        self.current_HP = n

    def getMaxHPStat(self):
        return self.MAX_HP

    def getPourcentageHP(self)->int:
        return int((self.current_HP / self.MAX_HP) * 100)

    def getAtkStat(self)->int:
        return self.atkStat

    def getDefStat(self)->int:
        return self.defStat

    def getSpaStat(self)->int:
        return self.spaStat

    def getSpdStat(self)->int:
        return self.spdStat

    def getSpeStat(self)->int:
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

    def applyDamage(self, damage)->None:
        """
        Apply a number of damage to the HP, if current HPs are lower to 0 then the pokemon is K.O.
        """
        self.current_HP -= damage
        if(self.current_HP < 0):
            self.current_HP = 0
            self.isKo = True

    def canMove(self)->bool:
        """
        Calcul if the pokemon can move dispite his status
        """
        return True

    def applyStatus(self):
        """
        Apply effects of the status to the pokemon
        """
        return

    def setStatus(self, statusPokemon)->bool: 
        """
        Change the instance to a decorator in order to apply a status
        @param the decorate pokemon
        """
        print(self.current_HP,"/",self.MAX_HP)
        self.trainer.setCurrentPokemon(statusPokemon)
        self = statusPokemon
        print(self.current_HP,"/",self.MAX_HP)

        return True

    def healStatus(self):
        """
        Transform the decorate instance to the pure instance in order to unset the status
        """
        return