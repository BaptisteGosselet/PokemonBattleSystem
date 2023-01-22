from model.status.Status import Status


class FreezeStatus(Status):

    def __init__(self):
        self.name = "Gelûre"
        self.abbreviation = "GEL"

    def applyStatus(self, pokemon):
        pokemon.applyDamage(int(pokemon.getMaxHP() // 16))

    def getStatusMessage(self) -> str:
        return "Le Pokémon est gelé."
