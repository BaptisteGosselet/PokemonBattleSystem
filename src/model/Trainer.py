class Trainer() :

    def __init__(self, name, pokemons):
        self.name = name
        
        self.currentPokemon = pokemons[0]
        self.team = []
        for i in range(1,len(pokemons)):
            self.team.append(pokemons[i])

    def getCurrentPokemon(self):
        return self.currentPokemon