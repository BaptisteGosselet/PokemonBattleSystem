from model.status.Status import Status


class FlinchStatus(Status):

    def __init__(self):
        self.name = "Peur"
        self.abbreviation = "PEUR"
        self.flinched = False

    def canMove(self)->bool:
        self.flinched = True
        return False

    def getFailMessage(self, pokemon) -> str:
        return "{} est apeuré.".format(pokemon.getName())

    def applyStatus(self, pokemon):
        if(self.flinched):
            pokemon.setStatus(None)

    def getStatusMessage(self) -> str:
        return ""
