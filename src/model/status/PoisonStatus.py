from random import randint
from model.status.Status import Status


class PoisonStatus(Status):

    def __init__(self):
        self.name = "Poison"
        self.abbreviation = "PSN"
        cpt = 1


    def applyStatus(self, pokemon):
        damage = int(pokemon.getMaxHP() * self.cpt // 16)
        cpt += 1
        pokemon.applyDamage(damage)


    def getStatusMessage(self) -> str:
        return "Le Pokémon est empoisonné."
