from model.TypePkmn import TypePkmn


class Move():

    def __init__(self, name, power, accuracy, type, isSpecial:bool, priority:int, sndEffect):

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
        categorie = "Statut"

        if(self.power == 0):
            return "Type : {}\n{}".format(self.type.getName(), categorie)


        if(self.isSpecial):
            categorie = "Special"
        else:
            categorie = "Physique"
        
        return "Puissance : {}\tType : {}\nPrécision : {}\t{}".format(self.power, self.type.getName(), self.accuracy, categorie)




        
