from model.PokemonFactory import PokemonFactory
from model.Pokemon import Pokemon
from model.status.ParalysisStatus import ParalysisStatus
from model.status.PoisonStatus import PoisonStatus
from model.move.Move import Move

def toto():
    print("toto")

def genererTypes_sol_electrik():
    pkmFactory = PokemonFactory()
    types = pkmFactory.getTypes()
    return types["sol"], types["electrik"]

def genererUnPokemon(name="pikachu"):
    pkmFact = PokemonFactory()
    return pkmFact.generatePokemon(name)

def genererPokemonAvecUnType(recherche):
    pkmFact = PokemonFactory()
    return Pokemon("Toto", pkmFact.getTypes()[recherche], None, 1, 1, 1, 1, 1, 1, None, None, None, None)

def genererParalysieEtPoison():
    return ParalysisStatus(), PoisonStatus()

def genererUnMove(prio=0):
        return Move("Charge", 40, 100, None, False, prio, None)
