from random import randint
from model.move.Move import Move

class MultipleMove(Move):

    def __init__(self, name, power, accuracy, type, isSpecial, priority, sndEffect, minHit=2, maxHit=5):
        super().__init__(name, power, accuracy, type, isSpecial, priority, sndEffect)
        self.power = self.power * randint(minHit, maxHit)

