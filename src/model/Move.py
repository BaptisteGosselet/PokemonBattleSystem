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

    def getName(self):
        return self.name

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getType(self):
        return self.type

    def getIsSpecial(self):
        return self.isSpecial

    def getPriority(self):
        return self.priority