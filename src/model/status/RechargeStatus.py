from random import randint
from model.status.Status import Status


class RechargeStatus(Status):

    def __init__(self):
        self.name = "Recharge"
        self.abbreviation = "RECHARGE"
        self.recharge = False

    def canMove(self)->bool:
        return False

    def canSwitch(self):
        return False

    def applyStatus(self, pokemon):
        if(self.recharge):
            pokemon.setStatus(None)
        else:
            self.recharge = True

    def getFailMessage(self, pokemon) -> str:
        return "{} doit se recharger".format(pokemon.getName())