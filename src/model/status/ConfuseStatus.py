from random import randint
from model.status.Status import Status


class ConfuseStatus(Status):

    def __init__(self):
        self.name = "Confusion"
        self.abbreviation = "CON"

        self.turn = 0
        self.confuseTurn = randint(1,4)
        self.fail = False

    def canMove(self)->bool:
        rand = randint(0,3)
        if(rand == 0):
            self.fail = True
        else:
            self.fail = False
        return self.fail

    def getFailMessage(self, pokemon) -> str:
        return "{} se frappe dans sa confusion !".format(pokemon.getName())

    def applyStatus(self, pokemon):
        if(self.fail):
            pokemon.applyDamage(20)
        if(self.turn >= self.confuseTurn):
            pokemon.setStatus(None)
        self.turn += 1

    def getStatusMessage(self) -> str:
        return "Le Pokémon s'endort."
