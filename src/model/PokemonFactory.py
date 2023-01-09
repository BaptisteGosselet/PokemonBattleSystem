from model.Pokemon import Pokemon

class PokemonFactory() : 

    def __init__(self):
        #init moves in a dictionnary
        #init types


        #Init Pokemon
        self.pokemons = {"dracaufeu": Pokemon("Dracaufeu", None, None, 78, 84, 78, 85, 85, 100, None, None), 
                    "leviator": Pokemon("Leviator", None, None, 95, 125, 79, 100, 100, 81, None, None), 
                    "grolem": Pokemon("Grolem", None, None, 80, 110, 130, 55, 55, 45, None, None), 
                    "alakazam": Pokemon("Alakazam", None, None, 55, 50, 45, 135, 135, 120, None, None), 
                    "ectoplasma": Pokemon("Ectoplasma", None, None, 60, 65, 60, 130, 130, 110, None, None),
                    "tauros": Pokemon("Tauros", None, None, 75, 100, 95, 70, 70, 110, None, None)
                }
        

    def getNamesList(self):
        return self.pokemons.keys()

    def generatePokemon(self, name):
        return self.pokemons[name.lower()]
