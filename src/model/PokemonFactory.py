from model.Pokemon import Pokemon

class PokemonFactory() : 

    def __init__(self):
        #init moves in a dictionnary
        #init types
        pass

    def generatePokemon(self, name):
        name = name.lower()
        if (name == "dracaufeu") : 
            return Pokemon("Dracaufeu", None, None, 78, 84, 78, 85, 85, 100, None, None)
        if (name == "leviator") : 
            return Pokemon("Leviator", None, None, 95, 125, 79, 100, 100, 81, None, None)
        if (name == "grolem") : 
            return Pokemon("Grolem", None, None, 80, 110, 130, 55, 55, 45, None, None)
        if (name == "alakazam") : 
            return Pokemon("Alakazam", None, None, 55, 50, 45, 135, 135, 120, None, None)    
        if (name == "ectoplasma") : 
            return Pokemon("Ectoplasma", None, None, 60, 65, 60, 130, 130, 110, None, None)
        if (name == "tauros") : 
            return Pokemon("Tauros", None, None, 75, 100, 95, 70, 70, 110, None, None)

