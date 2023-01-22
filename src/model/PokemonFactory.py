from model.move.Move import Move
from model.Pokemon import Pokemon
from model.TypePkmn import TypePkmn
from model.effect.HealAndRecoilEffect import HealAndRecoilEffect
from model.effect.StatChangeEffect import StatChangeEffect
from model.effect.StatusEffect import StatusEffect
from model.move.MultipleMove import MultipleMove
from model.status.BurnStatus import BurnStatus
from model.status.ConfuseStatus import ConfuseStatus
from model.status.FlinchStatus import FlinchStatus
from model.status.ParalysisStatus import ParalysisStatus
from model.status.PoisonStatus import PoisonStatus
from model.status.RechargeStatus import RechargeStatus
from model.status.SleepStatus import SleepStatus

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
            "deflagration":         Move("Déflagration",110,85,self.types["feu"], True, 0, StatusEffect(BurnStatus(),10)),
            "seisme" :              Move("Séisme", 100, 100, self.types["sol"], False, 0, None),
            "megacorne" :           Move("Mégacorne", 120, 85, self.types["insecte"], False, 0, None),
            "eboulement" :          Move("Eboulement", 75, 90, self.types["roche"], False, 0, None),
            "hydrocanon" :          Move("Hydrocanon", 120, 85, self.types["eau"], True, 0, None),
            "ultralaser" :          Move("Ultralaser", 150, 90, self.types["normal"], True, 0, StatusEffect(RechargeStatus(), 100, True)),
            "roc-boulet" :          Move("Roc-Boulet", 150, 90, self.types["roche"], False, 0, StatusEffect(RechargeStatus(), 100, True)),
            "plaquage" :            Move("Plaquage", 85, 100, self.types["normal"], False, 0, StatusEffect(ParalysisStatus(), 30)), 
            "psyko" :               Move("Psyko", 90, 100, self.types["psy"], 0, True, None),
            "cage-eclair" :         Move("Cage-Eclair", 0, 90, self.types["electrik"], False, 0, StatusEffect(ParalysisStatus(), 100)), 
            "toxik" :               Move("Toxik", 0, 90, self.types["poison"], False, 0, StatusEffect(PoisonStatus(), 100)), 
            "hypnose" :             Move("Hypnose", 0, 70, self.types["psy"], 0, False, StatusEffect(SleepStatus(), 100)),
            "ball'ombre":           Move("Ball'Ombre", 80, 100, self.types["spectre"], True, 0, StatChangeEffect([0,0,0,-1,0], 20)),
            "exploforce":           Move("Exploforce", 120, 70, self.types["combat"], True, 0, None),
            "psykoud'boul":         Move("Psykoud'boul", 80, 90, self.types["psy"], False, 0, StatusEffect(FlinchStatus(), 20)), 
            "bomb beurk":           Move("Bomb beurk", 90, 100, self.types["poison"], True, 0, StatusEffect(PoisonStatus(), 30)),
            "machouille":           Move("Machouille", 80, 100, self.types["tenebres"], False, 0, StatChangeEffect([0,-1,0,0,0], 20)),
            "cascade":              Move("Cascade", 80, 100, self.types["eau"], False, 0, StatusEffect(FlinchStatus(), 20)),
            "atterissage":          Move("Atterissage", 0, 100, self.types["vol"], False, 0, HealAndRecoilEffect(50, True)),
            "soin":                 Move("Soin", 0, 100, self.types["normal"], False, 0, HealAndRecoilEffect(50, True)),
            "e-coque":              Move("E-Coque", 0, 100, self.types["normal"], False, 0, HealAndRecoilEffect(50, True)),
            "explosion":            Move("Explosion", 250, 100, self.types["normal"], False, 0, HealAndRecoilEffect(-100, True)),
            "damocles":             Move("Damocles", 120, 100, self.types["normal"], False, 0, HealAndRecoilEffect(-25, True)),
            "danse draco":          Move("Danse Draco", 0, 100, self.types["dragon"], False, 0, StatChangeEffect([1,0,0,0,1], 100, True)),
            "enroulement":          Move("Enroulement", 0, 100, self.types["normal"], False, 0, StatChangeEffect([1,1,0,0,0], 100, True)),
            "malediction":          Move("Malédiction", 0, 100, self.types["spectre"], False, 0, StatChangeEffect([0,1,0,1,0], 100, True)),
            "tempete verte":        Move("Tempête Verte", 130, 90, self.types["plante"], True, 0, StatChangeEffect([0,0,-1,0,0], 100, True)),
            "detricanon":           Move("Détricanon", 120, 80, self.types["poison"], False, 0, StatusEffect(PoisonStatus(), 30)), 
            "canicule":             Move("Canicule", 95, 90, self.types["feu"], True, 0, StatusEffect(BurnStatus(), 10)), 
            "blizzard":             Move("Blizzard", 110, 75, self.types["glace"], True, 0, StatusEffect(BurnStatus(), 10)), #GEL
            "coup bas":             Move("Coup Bas", 70, 100, self.types["tenebres"], False, 1, None), 
            "double pied":          Move("Double Pied", 60, 100, self.types["combat"], False, 0, None), 
            "pc glace":             Move("Puissance Cachée", 60, 100, self.types["glace"], True, 0, None), 
            "pc feu":               Move("Puissance Cachée", 60, 100, self.types["feu"], True, 0, None), 
            "frappe atlas":         Move("Frappe Atlas", 100, 100, self.types["combat"], False, 0, None), 
            "exuviation" :          Move("Exuviation", 0, 100, self.types["normal"], False, 0, StatChangeEffect([1,-1,1,-1,1], 100, True)),
            "danse lames" :         Move("Danse Lames", 0, 100, self.types["normal"], False, 0, StatChangeEffect([2,0,0,0,0], 100, True)),
            "stalactite" :          MultipleMove("Stalactite", 25, 100, self.types["glace"], False, 0, None),
            "tonnerre" :            Move("Tonnerre", 90, 100, self.types["electrik"], True, 0, StatusEffect(ParalysisStatus(), 10)),
            "ebulition" :           Move("Ebulition", 90, 100, self.types["eau"], True, 0, StatusEffect(BurnStatus(), 30)),
            "laser glace" :         Move("Laser Glace", 90, 100, self.types["glace"], True, 0, StatusEffect(ParalysisStatus(), 10)), #GEL 
            "vent violent":         Move("Vent Violent", 110, 70, self.types["vol"], True, 0, StatusEffect(ConfuseStatus(), 20)) 

        }

        #Init Pokemon
        self.pokemons = {
            "dracaufeu" :   {"Nom":"Dracaufeu", "Type1":self.types["feu"], "Type2":self.types["vol"],
                            "PV":78, "ATK":84, "DEF":78, "SPA":109, "SPD":85, "SPE":100, 
                            "Move1":self.moves["deflagration"], "Move2":self.moves["vent violent"],
                            "Move3":self.moves["atterissage"], "Move4":self.moves["toxik"]}, 

            "leviator" :    {"Nom":"Leviator", "Type1":self.types["eau"], "Type2":self.types["vol"],
                            "PV":95, "ATK":125, "DEF":79, "SPA":60, "SPD":100, "SPE":81, 
                            "Move1":self.moves["danse draco"], "Move2":self.moves["cascade"],
                            "Move3":self.moves["seisme"], "Move4":self.moves["machouille"]},  

            "grolem" :      {"Nom":"Grolem", "Type1":self.types["sol"], "Type2":self.types["roche"],
                            "PV":80, "ATK":120, "DEF":130, "SPA":55, "SPD":65, "SPE":45, 
                            "Move1":self.moves["seisme"], "Move2":self.moves["eboulement"],
                            "Move3":self.moves["plaquage"], "Move4":self.moves["explosion"]}, 

            "alakazam" :    {"Nom":"Alakazam", "Type1":self.types["psy"], "Type2":None,
                            "PV":55, "ATK":50, "DEF":45, "SPA":135, "SPD":95, "SPE":120, 
                            "Move1":self.moves["psyko"], "Move2":self.moves["ball'ombre"],
                            "Move3":self.moves["exploforce"], "Move4":self.moves["cage-eclair"]},  

            "ectoplasma" :  {"Nom":"Ectoplasma", "Type1":self.types["spectre"], "Type2":self.types["poison"], 
                            "PV":60, "ATK":65, "DEF":60, "SPA":130, "SPD":75, "SPE":110, 
                            "Move1":self.moves["ball'ombre"], "Move2":self.moves["bomb beurk"],
                            "Move3":self.moves["exploforce"], "Move4":self.moves["hypnose"]}, 

            "arbok":       {"Nom":"Arbok", "Type1":self.types["poison"], "Type2":None, 
                            "PV":60, "ATK":95, "DEF":69, "SPA":65, "SPD":79, "SPE":80, 
                            "Move1":self.moves["enroulement"], "Move2":self.moves["detricanon"],
                            "Move3":self.moves["seisme"], "Move4":self.moves["coup bas"]},

            "crustabri":       {"Nom":"Crustabri", "Type1":self.types["eau"], "Type2":self.types["glace"], 
                            "PV":50, "ATK":95, "DEF":180, "SPA":85, "SPD":45, "SPE":70, 
                            "Move1":self.moves["exuviation"], "Move2":self.moves["stalactite"],
                            "Move3":self.moves["hydrocanon"], "Move4":self.moves["explosion"]},

            "staross":       {"Nom":"Staross", "Type1":self.types["eau"], "Type2":self.types["psy"], 
                            "PV":60, "ATK":75, "DEF":85, "SPA":100, "SPD":85, "SPE":115, 
                            "Move1":self.moves["hydrocanon"], "Move2":self.moves["tonnerre"],
                            "Move3":self.moves["laser glace"], "Move4":self.moves["soin"]},

            "flagadoss":     {"Nom":"Flagadoss", "Type1":self.types["eau"], "Type2":self.types["psy"], 
                            "PV":95, "ATK":75, "DEF":110, "SPA":100, "SPD":80, "SPE":30, 
                            "Move1":self.moves["ebulition"], "Move2":self.moves["psyko"],
                            "Move3":self.moves["laser glace"], "Move4":self.moves["soin"]},

            "voltali":     {"Nom":"Voltali", "Type1":self.types["electrik"], "Type2":None, 
                            "PV":65, "ATK":65, "DEF":60, "SPA":110, "SPD":95, "SPE":130, 
                            "Move1":self.moves["tonnerre"], "Move2":self.moves["ball'ombre"],
                            "Move3":self.moves["double pied"], "Move4":self.moves["cage-eclair"]},
            
            "leveinard":     {"Nom":"Leveinard", "Type1":self.types["normal"], "Type2":None, 
                            "PV":250, "ATK":5, "DEF":5, "SPA":35, "SPD":105, "SPE":50, 
                            "Move1":self.moves["frappe atlas"], "Move2":self.moves["laser glace"],
                            "Move3":self.moves["toxik"], "Move4":self.moves["e-coque"]},
            
            "rhinoferos":     {"Nom":"Rhinoferos", "Type1":self.types["roche"], "Type2":self.types["sol"], 
                            "PV":105, "ATK":130, "DEF":120, "SPA":45, "SPD":45, "SPE":40, 
                            "Move1":self.moves["roc-boulet"], "Move2":self.moves["seisme"],
                            "Move3":self.moves["megacorne"], "Move4":self.moves["danse lames"]},

            "noadkoko":     {"Nom":"Noadkoko", "Type1":self.types["plante"], "Type2":self.types["psy"], 
                            "PV":95, "ATK":95, "DEF":85, "SPA":125, "SPD":75, "SPE":55, 
                            "Move1":self.moves["tempete verte"], "Move2":self.moves["psyko"],
                            "Move3":self.moves["pc feu"], "Move4":self.moves["explosion"]},

            "electhor":     {"Nom":"Electhor", "Type1":self.types["electrik"], "Type2":self.types["vol"], 
                            "PV":90, "ATK":90, "DEF":85, "SPA":125, "SPD":90, "SPE":100, 
                            "Move1":self.moves["tonnerre"], "Move2":self.moves["canicule"],
                            "Move3":self.moves["pc glace"], "Move4":self.moves["atterissage"]},

            "ronflex":     {"Nom":"Ronflex", "Type1":self.types["normal"], "Type2":None, 
                            "PV":160, "ATK":110, "DEF":65, "SPA":65, "SPD":110, "SPE":30, 
                            "Move1":self.moves["damocles"], "Move2":self.moves["seisme"],
                            "Move3":self.moves["malediction"], "Move4":self.moves["soin"]},

            "lippoutou":     {"Nom":"Lippoutou", "Type1":self.types["glace"], "Type2":self.types["psy"], 
                            "PV":65, "ATK":50, "DEF":35, "SPA":115, "SPD":95, "SPE":95, 
                            "Move1":self.moves["blizzard"], "Move2":self.moves["psyko"],
                            "Move3":self.moves["exploforce"], "Move4":self.moves["hypnose"]},

            "tauros":       {"Nom":"Tauros", "Type1":self.types["normal"], "Type2":None, 
                            "PV":75, "ATK":100, "DEF":95, "SPA":40, "SPD":70, "SPE":110, 
                            "Move1":self.moves["plaquage"], "Move2":self.moves["seisme"],
                            "Move3":self.moves["deflagration"], "Move4":self.moves["psykoud'boul"]}
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

    def getNamesList(self)->list[str]:
        """
        return a list with names of all availables pokemon
        """
        return sorted(self.pokemons.keys())

    def generatePokemon(self, name):
        """
        Generate a pokemon from its name
        @param : pokemon's name
        """
        data = self.pokemons[name.lower()]
        return Pokemon(
            data["Nom"],
            data["Type1"], data["Type2"],
            data["PV"], data["ATK"], data["DEF"], data["SPA"], data["SPD"], data["SPE"],
            data["Move1"],data["Move2"],data["Move3"],data["Move4"])
