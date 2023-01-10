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

        self.isKo = False


    def getName(self):
        return self.name

    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getPourcentageHP(self):
        return int((self.current_HP / self.MAX_HP) * 100)

    def getAtkStat(self):
        return self.atkStat

    def getDefStat(self):
        return self.defStat

    def getSpaStat(self):
        return self.spaStat

    def getSpdStat(self):
        return self.spdStat

    def getSpeStat(self):
        return self.speStat

    def getIsKo(self):
        return self.isKo

    def getType1(self):
        return self.type1

    def getType2(self):
        return self.type2

    def applyDamage(self, damage):
        self.current_HP -= damage
        if(self.current_HP < 0):
            self.current_HP = 0
            self.isKo = True