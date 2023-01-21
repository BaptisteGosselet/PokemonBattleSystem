from random import randint
from model.status.Status import Status


class SleepStatus(Status):

    def __init__(self):
        self.name = "Sommeil"
        self.abbreviation = "SOM"

        self.turn = 0
        self.sleepTurn = randint(1,3)

    def canMove(self)->bool:
        return False

    def getFailMessage(self, pokemon) -> str:
        return "{} dort profondement...".format(pokemon.getName())

    def applyStatus(self, pokemon):
        if(self.turn >= self.sleepTurn):
            pokemon.setStatus(None)
        self.turn += 1