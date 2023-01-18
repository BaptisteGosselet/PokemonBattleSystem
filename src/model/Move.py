from model.TypePkmn import TypePkmn
from model.status.statusEffect.StatusEffect import StatusEffect


class Move():

    def __init__(self, name : str, power : int, accuracy : int, type : TypePkmn, isSpecial : bool, priority : int, sndEffect : StatusEffect):

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

    def applySecondaryEffect(self, pokemon)->bool:
        if(not self.sndEffect is None):
            return self.sndEffect.applyEffect(pokemon)
        return False

