from model.PokemonFactory import PokemonFactory

def toto():
    print("toto")

def genererTypes_sol_electrik():
    pkmFactory = PokemonFactory()
    types = pkmFactory.getTypes()
    return types["sol"], types["electrik"]
