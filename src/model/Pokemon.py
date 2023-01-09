class Pokemon : 

    def __init__(self, name, hp):
    
        self.name = name 
        self.MAX_HP = hp
        self.current_HP = hp


    def getName(self):
        return self.name

    def getPourcentageHP(self):
        return int((self.current_HP / self.MAX_HP) * 100)