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


    def getDescriptionText(self) -> str:
        """
        @return the description to display on hover the move button
        """
        if(self.isSpecial):
            return "Puissance : {}\nPrécision : {}\nSpécial".format(self.power, self.accuracy)
        elif(self.power == 0):
            return "Précision : {}\nStatut".format(self.accuracy)
        else:
            return "Puissance : {}\nPrécision : {}\nPhysique".format(self.power, self.accuracy)

        
