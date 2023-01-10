from model.Move import Move
from model.Pokemon import Pokemon

class PokemonFactory() : 

    def __init__(self):

        #init types

        #Init Moves
        self.moves = {
            "" : None,
            "deflagration":     Move("Déflagration",110,85,None, True, 0, None), #10% de brûlure
            "seisme" :          Move("Séisme", 100, 100, None, False, 0, None),
            "eboulement" :      Move("Eboulement", 75, 90, None, False, 0, None),
            "hydrocanon" :      Move("Hydrocanon", 120, 85, None, True, 0, None),
            "ultralaser" :      Move("Ultralaser", 150, 90, None, True, 0, None), #rechagement
            "plaquage" :        Move("Plaquage", 85, 100, None, False, 0, None), #30% de paralysie
            "psyko" :           Move("Psyko", 90, 100, None, 0, True, None),
            "cage-eclair" :     Move("Cage-Eclair", 0, 90, None, False, 0, None), #Paralysie 100% + attaque de status
            "hypnose" :         Move("Hypnose", 0, 70, None, 0, False, None), #sommeil 100% 
            "ball'ombre":       Move("Ball'Ombre", 80, 100, None, True, 0, None) #20% de baisse de def spé
        }

        #Init Pokemon
        self.pokemons = {
            "dracaufeu" :   {"Nom":"Dracaufeu", "Type1":None, "Type2":None, 
                            "PV":78, "ATK":84, "DEF":78, "SPA":85, "SPD":85, "SPE":100, 
                            "Move1":self.moves["deflagration"], "Move2":self.moves["seisme"]}, 
            "leviator" :    {"Nom":"Leviator", "Type1":None, "Type2":None, 
                            "PV":95, "ATK":125, "DEF":79, "SPA":100, "SPD":100, "SPE":81, 
                            "Move1":self.moves["hydrocanon"], "Move2":self.moves["ultralaser"]}, 
            "grolem" :      {"Nom":"Grolem", "Type1":None, "Type2":None, 
                            "PV":80, "ATK":110, "DEF":130, "SPA":55, "SPD":55, "SPE":45, 
                            "Move1":self.moves["seisme"], "Move2":self.moves["eboulement"]}, 
            "alakazam" :    {"Nom":"Alakazam", "Type1":None, "Type2":None, 
                            "PV":55, "ATK":50, "DEF":45, "SPA":135, "SPD":135, "SPE":120, 
                            "Move1":self.moves["psyko"], "Move2":self.moves["cage-eclair"]}, 
            "ectoplasma" :  {"Nom":"Ectoplasma", "Type1":None, "Type2":None, 
                            "PV":60, "ATK":65, "DEF":60, "SPA":130, "SPD":130, "SPE":110, 
                            "Move1":self.moves["ball'ombre"], "Move2":self.moves["hypnose"]},
            "tauros":       {"Nom":"Tauros", "Type1":None, "Type2":None, 
                            "PV":75, "ATK":100, "DEF":95, "SPA":70, "SPD":70, "SPE":110, 
                            "Move1":self.moves["plaquage"], "Move2":self.moves["ultralaser"]}
        }
        

    def getNamesList(self):
        return self.pokemons.keys()

    def generatePokemon(self, name):
        data = self.pokemons[name.lower()]
        return Pokemon(
            data["Nom"],
            data["Type1"], data["Type2"],
            data["PV"], data["ATK"], data["DEF"], data["SPA"], data["SPD"], data["SPE"],
            data["Move1"],data["Move2"])
