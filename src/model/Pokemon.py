class Pokemon : 

    def __init__(self, name, type1, type2,  hp, atkStat, defStat, spaStat, spdStat, speStat, move1, move2):
    
        self.name = name 
        self.type1 = type1
        self.type2 = type2
        
        self.MAX_HP = hp        
        self.current_HP = hp
        self.atkStat = atkStat
        self.defStat = defStat
        self.spaStat = spaStat
        self.spdStat = spdStat
        self.speStat = speStat

        self.move1 = move1
        self.move2 = move2


    def getName(self):
        return self.name

    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getPourcentageHP(self):
        return int((self.current_HP / self.MAX_HP) * 100)
