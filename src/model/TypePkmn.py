class TypePkmn: 
    def __init__(self, name):
        self.name = name
        self.weaknesses = []
        self.resistances = []
        self.immunities = []

    def getName(self)->str:
        return self.name

    def setWeaknesses(self, weaknesses)->None:
        self.weaknesses = weaknesses

    def setResistances(self, resistances)->None:
        self.resistances = resistances

    def setImmunities(self, immunities)->None:
        self.immunities = immunities

    def getMultiplicator(self, typ)->float:
        """
        Calculate a damage multiplicator regarding to weaknesses and resistances of this type
        """
        
        for i in self.immunities:
            if (i == typ):
                return 0

        for w in self.weaknesses:
            if (w == typ):
                return 2
        
        for r in self.resistances: 
            if (r == typ):
                return 0.5

        return 1
        