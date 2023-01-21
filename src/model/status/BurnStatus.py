from random import randint
from model.status.Status import Status


class BurnStatus(Status):

    def __init__(self):
        self.name = "Brûlure"
        self.abbreviation = "BRU"

    def applyStatus(self, pokemon):
        pokemon.applyDamage(int(pokemon.getMaxHP() // 16))