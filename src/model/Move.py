class Move():

    def __init__(self, name, power, accuracy, type, sndEffect):

        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.sndEffect = sndEffect
        #description : string ?

    def getName(self):
        return self.name