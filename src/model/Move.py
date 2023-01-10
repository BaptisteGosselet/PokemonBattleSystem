class Move():

    def __init__(self, name, power, accuracy, type, priority, sndEffect):

        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.priority = priority
        self.sndEffect = sndEffect
        #description : string ?

    def getName(self):
        return self.name

    def getPriority(self):
        return self.priority