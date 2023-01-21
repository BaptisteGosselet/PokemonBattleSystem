from random import randint
from model.status.Status import Status


class ParalysisStatus(Status):

    def __init__(self):
        self.name = "Paralysie"
        self.abbreviation = "PAR"

    def canMove(self)->bool:
        return (randint(0,100)<=75)

    def getFailMessage(self, pokemon) -> str:
        return "La Paralysie empêche {} de bouger.".format(pokemon.getName())