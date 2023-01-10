from model.Move import Move
from model.Pokemon import Pokemon
from model.TypePkmn import TypePkmn

class PokemonFactory() : 

    def __init__(self):

        #init types
        self.types = {
            "normal" :      TypePkmn("Normal"),
            "feu" :         TypePkmn("Feu"),
            "plante" :      TypePkmn("Plante"),
            "eau" :         TypePkmn("Eau"),
            "roche" :       TypePkmn("Roche"),
            "combat" :      TypePkmn("Combat"),
            "sol" :         TypePkmn("Sol"),
            "vol" :         TypePkmn("Vol"),
            "electrik" :    TypePkmn("Electrik"),
            "psy" :         TypePkmn("Psy"),
            "poison" :      TypePkmn("Poison"),
            "insecte" :     TypePkmn("Insecte"),
            "spectre" :     TypePkmn("Spectre"),
            "tenebres" :     TypePkmn("Tenebres"),
            "acier" :       TypePkmn("Acier"),
            "fee" :         TypePkmn("Fee"),
            "dragon" :      TypePkmn("Dragon"),
            "glace" :       TypePkmn("Glace")
        }

        self.initTypeTable()        

        #Init Moves
        self.moves = {
            "" : None,
            "deflagration":     Move("Déflagration",110,85,self.types["feu"], True, 0, None), #10% de brûlure
            "seisme" :          Move("Séisme", 100, 100, self.types["sol"], False, 0, None),
            "eboulement" :      Move("Eboulement", 75, 90, self.types["roche"], False, 0, None),
            "hydrocanon" :      Move("Hydrocanon", 120, 85, self.types["eau"], True, 0, None),
            "ultralaser" :      Move("Ultralaser", 150, 90, self.types["normal"], True, 0, None), #rechagement
            "plaquage" :        Move("Plaquage", 85, 100, self.types["normal"], False, 0, None), #30% de paralysie
            "psyko" :           Move("Psyko", 90, 100, self.types["psy"], 0, True, None),
            "cage-eclair" :     Move("Cage-Eclair", 0, 90, self.types["electrik"], False, 0, None), #Paralysie 100% + attaque de status
            "hypnose" :         Move("Hypnose", 0, 70, self.types["psy"], 0, False, None), #sommeil 100% 
            "ball'ombre":       Move("Ball'Ombre", 80, 100, self.types["spectre"], True, 0, None) #20% de baisse de def spé
        }

        #Init Pokemon
        self.pokemons = {
            "dracaufeu" :   {"Nom":"Dracaufeu", "Type1":self.types["feu"], "Type2":self.types["vol"], 
                            "PV":78, "ATK":84, "DEF":78, "SPA":109, "SPD":85, "SPE":100, 
                            "Move1":self.moves["deflagration"], "Move2":self.moves["seisme"]}, 
            "leviator" :    {"Nom":"Leviator", "Type1":self.types["eau"], "Type2":self.types["vol"], 
                            "PV":95, "ATK":125, "DEF":79, "SPA":60, "SPD":100, "SPE":81, 
                            "Move1":self.moves["hydrocanon"], "Move2":self.moves["ultralaser"]}, 
            "grolem" :      {"Nom":"Grolem", "Type1":self.types["sol"], "Type2":self.types["roche"], 
                            "PV":80, "ATK":120, "DEF":130, "SPA":55, "SPD":65, "SPE":45, 
                            "Move1":self.moves["seisme"], "Move2":self.moves["eboulement"]}, 
            "alakazam" :    {"Nom":"Alakazam", "Type1":self.types["psy"], "Type2":None, 
                            "PV":55, "ATK":50, "DEF":45, "SPA":135, "SPD":95, "SPE":120, 
                            "Move1":self.moves["psyko"], "Move2":self.moves["cage-eclair"]}, 
            "ectoplasma" :  {"Nom":"Ectoplasma", "Type1":self.types["spectre"], "Type2":self.types["poison"], 
                            "PV":60, "ATK":65, "DEF":60, "SPA":130, "SPD":75, "SPE":110, 
                            "Move1":self.moves["ball'ombre"], "Move2":self.moves["hypnose"]},
            "tauros":       {"Nom":"Tauros", "Type1":self.types["normal"], "Type2":None, 
                            "PV":75, "ATK":100, "DEF":95, "SPA":40, "SPD":70, "SPE":110, 
                            "Move1":self.moves["plaquage"], "Move2":self.moves["ultralaser"]}
        }
        
    def initTypeTable(self):
        
        self.types["normal"].setWeaknesses([self.types["combat"]])
        self.types["normal"].setImmunities([self.types["spectre"]])        
        self.types["feu"].setWeaknesses([self.types["eau"],self.types["roche"],self.types["sol"]])
        self.types["feu"].setResistances([self.types["feu"],self.types["insecte"],self.types["plante"]])
        self.types["plante"].setWeaknesses([self.types["feu"],self.types["glace"],self.types["insecte"],self.types["poison"],self.types["vol"]])
        self.types["plante"].setResistances([self.types["eau"],self.types["electrik"],self.types["plante"],self.types["sol"]])
        self.types["eau"].setWeaknesses([self.types["electrik"],self.types["plante"]])
        self.types["eau"].setResistances([self.types["acier"],self.types["eau"],self.types["feu"],self.types["glace"]])        
        self.types["roche"].setWeaknesses([self.types["acier"],self.types["combat"],self.types["eau"],self.types["plante"],self.types["sol"]])
        self.types["roche"].setResistances([self.types["feu"],self.types["normal"],self.types["poison"],self.types["vol"]])        
        self.types["sol"].setWeaknesses([self.types["eau"],self.types["glace"],self.types["plante"]])
        self.types["sol"].setResistances([self.types["poison"],self.types["roche"]])
        self.types["sol"].setImmunities([self.types["electrik"]])
        self.types["combat"].setWeaknesses([self.types["psy"],self.types["vol"]])
        self.types["combat"].setResistances([self.types["insecte"],self.types["roche"],self.types["tenebres"]])
        self.types["vol"].setWeaknesses([self.types["electrik"],self.types["glace"],self.types["roche"]])
        self.types["vol"].setResistances([self.types["combat"],self.types["insecte"],self.types["plante"]])
        self.types["vol"].setImmunities([self.types["sol"]])
        self.types["electrik"].setWeaknesses([self.types["sol"]])
        self.types["electrik"].setResistances([self.types["electrik"],self.types["vol"]])
        self.types["psy"].setWeaknesses([self.types["insecte"],self.types["spectre"],self.types["tenebres"]])
        self.types["psy"].setResistances([self.types["combat"],self.types["psy"]])
        self.types["poison"].setWeaknesses([self.types["psy"],self.types["sol"]])
        self.types["poison"].setResistances([self.types["combat"],self.types["fee"],self.types["insecte"],self.types["plante"],self.types["poison"]])
        self.types["insecte"].setWeaknesses([self.types["feu"], self.types["roche"],self.types["vol"]])
        self.types["insecte"].setResistances([self.types["combat"],self.types["plante"],self.types["sol"]])
        self.types["spectre"].setWeaknesses([self.types["spectre"], self.types["tenebres"]])
        self.types["spectre"].setResistances([self.types["insecte"], self.types["poison"]])
        self.types["spectre"].setImmunities([self.types["combat"], self.types["normal"]])
        self.types["tenebres"].setWeaknesses([self.types["combat"],self.types["fee"], self.types["insecte"]])
        self.types["tenebres"].setResistances([self.types["spectre"],self.types["tenebres"]])
        self.types["tenebres"].setImmunities([self.types["psy"]])
        self.types["acier"].setWeaknesses([self.types["combat"],self.types["feu"],self.types["sol"]])
        self.types["acier"].setResistances([self.types["acier"],self.types["dragon"],self.types["glace"],self.types["insecte"],self.types["fee"],self.types["normal"],self.types["plante"],self.types["psy"],self.types["roche"],self.types["vol"]])
        self.types["acier"].setImmunities([self.types["poison"]])
        self.types["fee"].setWeaknesses([self.types["acier"],self.types["poison"]])
        self.types["fee"].setResistances([self.types["combat"],self.types["insecte"],self.types["tenebres"]])
        self.types["fee"].setImmunities([self.types["dragon"]])
        self.types["dragon"].setWeaknesses([self.types["dragon"],self.types["fee"],self.types["glace"]])
        self.types["dragon"].setResistances([self.types["eau"],self.types["plante"],self.types["feu"],self.types["electrik"]])
        self.types["glace"].setWeaknesses([self.types["combat"],self.types["feu"],self.types["roche"]])
        self.types["glace"].setResistances([self.types["glace"]])

    def getNamesList(self):
        return self.pokemons.keys()

    def generatePokemon(self, name):
        data = self.pokemons[name.lower()]
        return Pokemon(
            data["Nom"],
            data["Type1"], data["Type2"],
            data["PV"], data["ATK"], data["DEF"], data["SPA"], data["SPD"], data["SPE"],
            data["Move1"],data["Move2"])
