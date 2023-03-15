from model.PokemonFactory import PokemonFactory
from model.TypePkmn import TypePkmn
from model.effect.StatusEffect import StatusEffect
from model.move.Move import Move
from model.status.ParalysisStatus import ParalysisStatus

class MockFactory(PokemonFactory) : 

    def __init__(self):

        #init types
        self.types = {
            "normal" : TypePkmn("Normal"),
            "combat" : TypePkmn("Combat"),
            "spectre" : TypePkmn("Spectre"),
        }

        self.initTypeTable()        

        #Init Moves
        self.moves = {
            "" : None,
            "plaquage" : Move("Plaquage", 85, 100, self.types["normal"], False, 0, StatusEffect(ParalysisStatus(), 30)), 
        }

        #Init Pokemon
        self.pokemons = {
            "tauros":       {"Nom":"Tauros", "Type1":self.types["normal"], "Type2":None, 
                            "PV":75, "ATK":100, "DEF":95, "SPA":40, "SPD":70, "SPE":110, 
                            "Move1":self.moves["plaquage"], "Move2":self.moves[""],
                            "Move3":self.moves[""], "Move4":self.moves[""]}
        }
        
    def initTypeTable(self):
        
        self.types["normal"].setWeaknesses([self.types["combat"]])
        self.types["normal"].setImmunities([self.types["spectre"]])        
