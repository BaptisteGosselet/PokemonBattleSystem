from model.TypePkmn import TypePkmn


class Move():

    def __init__(self, name, power, accuracy, type, isSpecial, priority, sndEffect):

        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.isSpecial = isSpecial
        self.priority = priority
        self.sndEffect = sndEffect
        #description : string ?

    def getName(self) -> str:
        return self.name

    def getPower(self) -> int:
        return self.power

    def getAccuracy(self) -> int:
        return self.accuracy

    def getType(self) -> TypePkmn :
        return self.type

    def getIsSpecial(self) -> bool:
        return self.isSpecial

    def getPriority(self) -> int:
        return self.priority

    def getSndEffect(self) : 
        return self.sndEffect
