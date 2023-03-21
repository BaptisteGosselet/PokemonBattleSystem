from model.PokemonFactory import PokemonFactory
from model.Pokemon import Pokemon

def toto():
    print("toto")

def genererTypes_sol_electrik():
    pkmFactory = PokemonFactory()
    types = pkmFactory.getTypes()
    return types["sol"], types["electrik"]

def genererUnPokemon():
    pkmFact = PokemonFactory()
    return pkmFact.generatePokemon("pikachu")

def genererPokemonAvecUnType(recherche):
    pkmFact = PokemonFactory()
    return Pokemon("Toto", pkmFact.getTypes()[recherche], None, 1, 1, 1, 1, 1, 1, None, None, None, None)