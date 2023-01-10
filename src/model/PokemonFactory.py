from model.Move import Move
from model.Pokemon import Pokemon

class PokemonFactory() : 

    def __init__(self):

        #init types

        #Init Moves
        self.moves = {
            "" : None,
            "deflagration":     Move("Déflagration",110,85,None, 0, None), #10% de brûlure
            "seisme" :          Move("Séisme", 100, 100, None, 0, None),
            "eboulement" :      Move("Eboulement", 75, 90, None, 0, None),
            "hydrocanon" :      Move("Hydrocanon", 120, 85, None, 0, None),
            "ultralaser" :      Move("Ultralaser", 150, 90, None, 0, None), #rechagement
            "plaquage" :        Move("Plaquage", 85, 100, None, 0, None), #30% de paralysie
            "psyko" :           Move("Psyko", 90, 100, None, 0, None),
            "cage-eclair" :     Move("Cage-Eclair", 0, 90, None, 0, None), #Paralysie 100% + attaque de status
            "hypnose" :         Move("Hypnose", 0, 70, None, 0, None), #sommeil 100% 
            "ball'ombre":       Move("Ball'Ombre", 80, 100, None, 0, None) #20% de baisse de def spé
        }

        #Init Pokemon
        self.pokemons = {
            "dracaufeu" :   Pokemon("Dracaufeu", None, None, 78, 84, 78, 85, 85, 100, self.moves["deflagration"], self.moves["seisme"]), 
            "leviator" :    Pokemon("Leviator", None, None, 95, 125, 79, 100, 100, 81, self.moves["hydrocanon"], self.moves["ultralaser"]), 
            "grolem" :      Pokemon("Grolem", None, None, 80, 110, 130, 55, 55, 45, self.moves["seisme"], self.moves["eboulement"]), 
            "alakazam" :    Pokemon("Alakazam", None, None, 55, 50, 45, 135, 135, 120, self.moves["psyko"], self.moves["cage-eclair"]), 
            "ectoplasma" :  Pokemon("Ectoplasma", None, None, 60, 65, 60, 130, 130, 110, self.moves["ball'ombre"], self.moves["hypnose"]),
            "tauros":       Pokemon("Tauros", None, None, 75, 100, 95, 70, 70, 110, self.moves["plaquage"], self.moves["ultralaser"])
        }
        

    def getNamesList(self):
        return self.pokemons.keys()

    def generatePokemon(self, name):
        return self.pokemons[name.lower()]
