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
from model.status.FreezeStatus import FreezeStatus
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
            "close combat":         Move("Close Combat", 120, 100, self.types["combat"], False, 0, StatChangeEffect([0,-1,0,-1,0], 100, True)),
            "sabotage":             Move("Sabotage", 80, 100, self.types["tenebres"], False, 0, None),
            "pisto-poing":          Move("Pisto Poing", 40, 100, self.types["acier"], False, 1, None),
            "pouvoir lunaire":      Move("Pouvoir Lunaire", 95, 100, self.types["fee"], True, 0, StatChangeEffect([0,0,-1,0,0], 30, False)),
            "osmerang" :            MultipleMove("Osmerang", 50, 100, self.types["sol"], False, 0, None, 1, 2),
            "lame de roc":          Move("Lame de Roc",100,80,self.types["roche"], False, 0, None),
            "os ombre":             Move("Os Ombre", 85, 100, self.types["spectre"], False, 0, StatChangeEffect([0,-1,0,0,0], 20, False)),
            "boutefeu":             Move("Boutefeu", 120, 100, self.types["feu"], False, 0, HealAndRecoilEffect(-33, True)),
            "liquidation":          Move("Liquidation", 85, 100, self.types["eau"], False, 0, StatChangeEffect([0,-1,0,0,0], 20, False)),
            "surpuissance":         Move("Surpuissance", 120, 100, self.types["combat"], False, 0, StatChangeEffect([-1,-1,0,0,0], 100, True)),
            "tour rapide":          Move("Tour Rapide", 40, 100, self.types["normal"], False, 0, StatChangeEffect([0,0,0,0,1], 100, True)),
            "acidearmure":          Move("Acidarmure", 0, 100, self.types["poison"], False, 0, StatChangeEffect([0,2,0,0,0], 100, True)),
            "ombre portee":         Move("Ombre Portée",40,100,self.types["spectre"], False, 1, None),
            "agilite" :             Move("Agilité", 0, 100, self.types["psy"], False, 0, StatChangeEffect([0,0,0,0,2], 100, True)),
            "regard glacant" :      Move("Regard Glaçant", 90, 100, self.types["psy"], True, 0, StatusEffect(FreezeStatus(), 10)),
            "fureur ardente":       Move("Fureur Ardente", 90, 100, self.types["tenebres"], True, 0, StatusEffect(FlinchStatus(),20)),
            "aurore":               Move("Aurore", 0, 100, self.types["normal"], False, 0, HealAndRecoilEffect(50, True)),
            "luminocanon":          Move("Luminocanon", 80, 100, self.types["acier"], True, 0, StatChangeEffect([0,0,0,-1,0], 10, False)),
            "rayon charge":         Move("Rayon Chargé", 50, 90, self.types["electrik"], True, 0, StatChangeEffect([0,0,1,0,0], 70, True)),
            "colere":               Move("Colere", 120, 100, self.types["dragon"], False, 0, StatusEffect(ConfuseStatus(),100, True)),
            "poing feu" :           Move("Poing de Feu", 75, 100, self.types["feu"], False, 0, StatusEffect(BurnStatus(), 10)),
            "direct toxic" :        Move("Direct Toxic", 80, 100, self.types["poison"], False, 0, StatusEffect(PoisonStatus(), 30)),
            "casse brique" :        Move("Casse Brique", 75, 100, self.types["combat"], False, 0, None),
            "plaie croix" :         Move("Plaie Croix", 80, 100, self.types["insecte"], False, 0, None),
            "aeropique" :          Move("Aeropique", 60, 200, self.types["vol"], False, 0, None),
            "plenitude" :           Move("Plenitude", 0, 100, self.types["psy"], False, 0, StatChangeEffect([0,0,1,1,0], 100, True)),
            "eco-sphere":           Move("Eco-Sphere", 90, 100, self.types["plante"], True, 0, StatChangeEffect([0,0,0,-1,0], 10, False)),
            "croissance":           Move("Croissance", 0, 100, self.types["plante"], False, 0, StatChangeEffect([1,1,0,0,0], 100, True)),
            "synthese":             Move("Synthese", 0, 100, self.types["plante"], False, 0, HealAndRecoilEffect(50, True)),
            "aurasphere":           Move("Aurasphere", 80, 100, self.types["combat"], True, 0, None),
            "vibrobscur":           Move("Vibrobscur", 80, 100, self.types["tenebres"], True, 0, StatusEffect(FlinchStatus(),20)),
            "feu follet" :          Move("Feu follet", 0, 85, self.types["feu"], False, 0, StatusEffect(BurnStatus(), 100)), 
            "lance-flammes" :       Move("Lance-flammes", 90, 100, self.types["feu"], True, 0, StatusEffect(BurnStatus(), 10)),
            "croc fatal":           Move("Croc Fatal", 0, 100, self.types["normal"], False, 0, HealAndRecoilEffect(-50, False)),
            "fatal foudre" :        Move("Fatal Foudre", 110, 70, self.types["electrik"], True, 0, StatusEffect(ParalysisStatus(), 30)),
            "surf" :                Move("Surf", 90, 100, self.types["eau"], True, 0, None),
            "electacle":            Move("Electacle", 120, 100, self.types["electrik"], False, 0, HealAndRecoilEffect(-10, True)),
            "vive attaque":         Move("Vive attaque",40,100,self.types["normal"], False, 1, None),
            "vitesse extreme":      Move("Vitesse Extrême",80,100,self.types["normal"], False, 2, None),
            "deflagration":         Move("Déflagration",110,85,self.types["feu"], True, 0, StatusEffect(BurnStatus(),10)),
            "cradovague":           Move("Cradovague",95,100,self.types["poison"], True, 0, StatusEffect(PoisonStatus(),10)),
            "telluriforce":         Move("Telluriforce",90,100,self.types["sol"], True, 0, StatChangeEffect([0,0,0,0,-1,0],10)),
            "eboulement":           Move("Eboulement",110,85,self.types["roche"], False, 0, StatusEffect(FlinchStatus(),10)),
            "seisme" :              Move("Séisme", 100, 100, self.types["sol"], False, 0, None),
            "megacorne" :           Move("Mégacorne", 120, 85, self.types["insecte"], False, 0, None),
            "eboulement" :          Move("Eboulement", 75, 90, self.types["roche"], False, 0, None),
            "hydrocanon" :          Move("Hydrocanon", 120, 85, self.types["eau"], True, 0, None),
            "ultralaser" :          Move("Ultralaser", 150, 90, self.types["normal"], True, 0, StatusEffect(RechargeStatus(), 100, True)),
            "roc-boulet" :          Move("Roc-Boulet", 150, 90, self.types["roche"], False, 0, StatusEffect(RechargeStatus(), 100, True)),
            "plaquage" :            Move("Plaquage", 85, 100, self.types["normal"], False, 0, StatusEffect(ParalysisStatus(), 30)), 
            "psyko" :               Move("Psyko", 90, 100, self.types["psy"], True, 0, None),
            "extrasenseur" :        Move("Extrasenseur", 80, 100, self.types["psy"], True, 0, StatusEffect(FlinchStatus(),10)),
            "cage-eclair" :         Move("Cage-Eclair", 0, 90, self.types["electrik"], False, 0, StatusEffect(ParalysisStatus(), 100)), 
            "toxik" :               Move("Toxik", 0, 90, self.types["poison"], False, 0, StatusEffect(PoisonStatus(), 100)), 
            "hypnose" :             Move("Hypnose", 0, 70, self.types["psy"], False, 0, StatusEffect(SleepStatus(), 100)),
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
            "machination":          Move("Machination", 0, 100, self.types["tenebres"], False, 0, StatChangeEffect([0,0,2,0,0], 100, True)),
            "malediction":          Move("Malédiction", 0, 100, self.types["spectre"], False, 0, StatChangeEffect([0,1,0,1,0], 100, True)),
            "tempete verte":        Move("Tempête Verte", 130, 90, self.types["plante"], True, 0, StatChangeEffect([0,0,-1,0,0], 100, True)),
            "detricanon":           Move("Détricanon", 120, 80, self.types["poison"], False, 0, StatusEffect(PoisonStatus(), 30)), 
            "canicule":             Move("Canicule", 95, 90, self.types["feu"], True, 0, StatusEffect(BurnStatus(), 10)), 
            "blizzard":             Move("Blizzard", 110, 75, self.types["glace"], True, 0, StatusEffect(FreezeStatus(), 10)),
            "coup bas":             Move("Coup Bas", 70, 100, self.types["tenebres"], False, 1, None), 
            "double pied":          Move("Double Pied", 60, 100, self.types["combat"], False, 0, None), 
            "pc glace":             Move("Puissance Cachée", 60, 100, self.types["glace"], True, 0, None), 
            "pc plante":            Move("Puissance Cachée", 60, 100, self.types["plante"], True, 0, None), 
            "pc eau":               Move("Puissance Cachée", 60, 100, self.types["eau"], True, 0, None), 
            "pc feu":               Move("Puissance Cachée", 60, 100, self.types["feu"], True, 0, None), 
            "frappe atlas":         Move("Frappe Atlas", 100, 100, self.types["combat"], False, 0, None), 
            "exuviation" :          Move("Exuviation", 0, 100, self.types["normal"], False, 0, StatChangeEffect([1,-1,1,-1,1], 100, True)),
            "danse lames" :         Move("Danse Lames", 0, 100, self.types["normal"], False, 0, StatChangeEffect([2,0,0,0,0], 100, True)),
            "stalactite" :          MultipleMove("Stalactite", 25, 100, self.types["glace"], False, 0, None),
            "tonnerre" :            Move("Tonnerre", 90, 100, self.types["electrik"], True, 0, StatusEffect(ParalysisStatus(), 10)),
            "ebulition" :           Move("Ebulition", 90, 100, self.types["eau"], True, 0, StatusEffect(BurnStatus(), 30)),
            "laser glace" :         Move("Laser Glace", 90, 100, self.types["glace"], True, 0, StatusEffect(FreezeStatus(), 10)), 
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
                            "Move3":self.moves["ombre portee"], "Move4":self.moves["hypnose"]}, 

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

            "nidoking":     {"Nom":"Nidoking", "Type1":self.types["sol"], "Type2":self.types["poison"], 
                            "PV":91, "ATK":102, "DEF":77, "SPA":85, "SPD":75, "SPE":85, 
                            "Move1":self.moves["cradovague"], "Move2":self.moves["telluriforce"],
                            "Move3":self.moves["tonnerre"], "Move4":self.moves["eboulement"]},

            "pikachu":     {"Nom":"Pikachu", "Type1":self.types["electrik"], "Type2":None, 
                            "PV":35, "ATK":110, "DEF":40, "SPA":100, "SPD":50, "SPE":50, 
                            "Move1":self.moves["vitesse extreme"], "Move2":self.moves["tonnerre"],
                            "Move3":self.moves["electacle"], "Move4":self.moves["surf"]},

            "raichu":     {"Nom":"Raichu", "Type1":self.types["electrik"], "Type2":self.types["psy"], 
                            "PV":60, "ATK":85, "DEF":50, "SPA":95, "SPD":85, "SPE":110, 
                            "Move1":self.moves["fatal foudre"], "Move2":self.moves["machination"],
                            "Move3":self.moves["psyko"], "Move4":self.moves["exploforce"]},

            "rattatak":     {"Nom":"Rattatak", "Type1":self.types["normal"], "Type2":None, 
                            "PV":55, "ATK":81, "DEF":60, "SPA":50, "SPD":50, "SPE":97, 
                            "Move1":self.moves["ultralaser"], "Move2":self.moves["croc fatal"],
                            "Move3":self.moves["coup bas"], "Move4":self.moves["danse lames"]},

            "smogogo":     {"Nom":"Smogogo", "Type1":self.types["poison"], "Type2":None, 
                            "PV":65, "ATK":90, "DEF":120, "SPA":85, "SPD":70, "SPE":60, 
                            "Move1":self.moves["bomb beurk"], "Move2":self.moves["lance-flammes"],
                            "Move3":self.moves["feu follet"], "Move4":self.moves["explosion"]},

            "roucarnage":     {"Nom":"Roucarnage", "Type1":self.types["vol"], "Type2":self.types["normal"], 
                            "PV":83, "ATK":80, "DEF":75, "SPA":70, "SPD":70, "SPE":101, 
                            "Move1":self.moves["vent violent"], "Move2":self.moves["canicule"],
                            "Move3":self.moves["vive attaque"], "Move4":self.moves["atterissage"]},

            "tortank":     {"Nom":"Tortank", "Type1":self.types["eau"], "Type2":None, 
                            "PV":79, "ATK":83, "DEF":100, "SPA":85, "SPD":105, "SPE":78, 
                            "Move1":self.moves["hydrocanon"], "Move2":self.moves["vibrobscur"],
                            "Move3":self.moves["aurasphere"], "Move4":self.moves["laser glace"]},

            "florizarre":     {"Nom":"Florizarre", "Type1":self.types["plante"], "Type2":self.types["poison"], 
                            "PV":80, "ATK":82, "DEF":83, "SPA":100, "SPD":100, "SPE":80, 
                            "Move1":self.moves["eco-sphere"], "Move2":self.moves["bomb beurk"],
                            "Move3":self.moves["croissance"], "Move4":self.moves["synthese"]},

            "locklass":     {"Nom":"Locklass", "Type1":self.types["eau"], "Type2":self.types["glace"], 
                            "PV":130, "ATK":85, "DEF":80, "SPA":95, "SPD":95, "SPE":60, 
                            "Move1":self.moves["blizzard"], "Move2":self.moves["tonnerre"],
                            "Move3":self.moves["plaquage"], "Move4":self.moves["ultralaser"]},

            "mewtwo":     {"Nom":"Mewtwo", "Type1":self.types["psy"], "Type2":None, 
                            "PV":106, "ATK":110, "DEF":90, "SPA":154, "SPD":90, "SPE":130, 
                            "Move1":self.moves["psyko"], "Move2":self.moves["plenitude"],
                            "Move3":self.moves["laser glace"], "Move4":self.moves["aurasphere"]},

            "feunard":     {"Nom":"Feunard", "Type1":self.types["feu"], "Type2":None, 
                            "PV":73, "ATK":76, "DEF":75, "SPA":81, "SPD":100, "SPE":100, 
                            "Move1":self.moves["deflagration"], "Move2":self.moves["machination"],
                            "Move3":self.moves["eco-sphere"], "Move4":self.moves["extrasenseur"]},

            "mackogneur":     {"Nom":"Mackogneur", "Type1":self.types["combat"], "Type2":None, 
                            "PV":90, "ATK":130, "DEF":80, "SPA":65, "SPD":85, "SPE":55, 
                            "Move1":self.moves["close combat"], "Move2":self.moves["sabotage"],
                            "Move3":self.moves["pisto-poing"], "Move4":self.moves["eboulement"]},

            "melodelfe":     {"Nom":"Melodelfe", "Type1":self.types["fee"], "Type2":None, 
                            "PV":90, "ATK":70, "DEF":73, "SPA":95, "SPD":90, "SPE":60, 
                            "Move1":self.moves["pouvoir lunaire"], "Move2":self.moves["e-coque"],
                            "Move3":self.moves["cage-eclair"], "Move4":self.moves["plenitude"]},

            "ossatueur":     {"Nom":"Ossatueur", "Type1":self.types["sol"], "Type2":None, 
                            "PV":60, "ATK":80, "DEF":110, "SPA":50, "SPD":80, "SPE":45, 
                            "Move1":self.moves["osmerang"], "Move2":self.moves["lame de roc"],
                            "Move3":self.moves["os ombre"], "Move4":self.moves["boutefeu"]},

            "kabutops":     {"Nom":"Kabutops", "Type1":self.types["eau"], "Type2":self.types["roche"], 
                            "PV":60, "ATK":115, "DEF":105, "SPA":65, "SPD":70, "SPE":80, 
                            "Move1":self.moves["liquidation"], "Move2":self.moves["lame de roc"],
                            "Move3":self.moves["surpuissance"], "Move4":self.moves["tour rapide"]},

            "aquali":     {"Nom":"Aquali", "Type1":self.types["eau"], "Type2":None, 
                            "PV":130, "ATK":65, "DEF":60, "SPA":110, "SPD":95, "SPE":65, 
                            "Move1":self.moves["ebulition"], "Move2":self.moves["laser glace"],
                            "Move3":self.moves["pc plante"], "Move4":self.moves["acidearmure"]},

            "pyroli":     {"Nom":"Pyroli", "Type1":self.types["feu"], "Type2":None, 
                            "PV":65, "ATK":130, "DEF":60, "SPA":95, "SPD":110, "SPE":65, 
                            "Move1":self.moves["boutefeu"], "Move2":self.moves["surpuissance"],
                            "Move3":self.moves["damocles"], "Move4":self.moves["vive attaque"]},

            "artikodin":     {"Nom":"Artikodin", "Type1":self.types["glace"], "Type2":self.types["vol"], 
                            "PV":90, "ATK":85, "DEF":100, "SPA":95, "SPD":125, "SPE":85, 
                            "Move1":self.moves["vent violent"], "Move2":self.moves["laser glace"],
                            "Move3":self.moves["agilite"], "Move4":self.moves["regard glacant"]},

            "sulfura":     {"Nom":"Sulfura", "Type1":self.types["feu"], "Type2":self.types["vol"], 
                            "PV":90, "ATK":100, "DEF":90, "SPA":125, "SPD":85, "SPE":90, 
                            "Move1":self.moves["vent violent"], "Move2":self.moves["deflagration"],
                            "Move3":self.moves["agilite"], "Move4":self.moves["fureur ardente"]},

            "arcanin":     {"Nom":"Arcanin", "Type1":self.types["feu"], "Type2":None, 
                            "PV":90, "ATK":110, "DEF":80, "SPA":100, "SPD":80, "SPE":95, 
                            "Move1":self.moves["boutefeu"], "Move2":self.moves["electacle"],
                            "Move3":self.moves["vitesse extreme"], "Move4":self.moves["aurore"]},

            "magneton":     {"Nom":"Magneton", "Type1":self.types["electrik"], "Type2":self.types["acier"], 
                            "PV":50, "ATK":60, "DEF":95, "SPA":120, "SPD":70, "SPE":70, 
                            "Move1":self.moves["fatal foudre"], "Move2":self.moves["pc feu"],
                            "Move3":self.moves["luminocanon"], "Move4":self.moves["toxik"]},

            "electrode":     {"Nom":"Electrode", "Type1":self.types["electrik"], "Type2":None, 
                            "PV":60, "ATK":50, "DEF":70, "SPA":80, "SPD":80, "SPE":150, 
                            "Move1":self.moves["rayon charge"], "Move2":self.moves["explosion"],
                            "Move3":self.moves["cage-eclair"], "Move4":self.moves["pc eau"]},

            "dracolosse":     {"Nom":"Dracolosse", "Type1":self.types["dragon"], "Type2":self.types["vol"], 
                            "PV":91, "ATK":134, "DEF":95, "SPA":100, "SPD":100, "SPE":80, 
                            "Move1":self.moves["danse draco"], "Move2":self.moves["colere"],
                            "Move3":self.moves["poing feu"], "Move4":self.moves["vitesse extreme"]},

            "grotadmorv":     {"Nom":"Grotadmorv", "Type1":self.types["poison"], "Type2":None, 
                            "PV":105, "ATK":105, "DEF":75, "SPA":65, "SPD":100, "SPE":50, 
                            "Move1":self.moves["direct toxic"], "Move2":self.moves["casse brique"],
                            "Move3":self.moves["ombre portee"], "Move4":self.moves["explosion"]},

            "insecateur":     {"Nom":"Insecateur", "Type1":self.types["insecte"], "Type2":self.types["vol"], 
                            "PV":91, "ATK":134, "DEF":95, "SPA":100, "SPD":100, "SPE":80, 
                            "Move1":self.moves["plaie croix"], "Move2":self.moves["aeropique"],
                            "Move3":self.moves["danse lames"], "Move4":self.moves["atterissage"]},

            "tauros":       {"Nom":"Tauros", "Type1":self.types["normal"], "Type2":None, 
                            "PV":75, "ATK":100, "DEF":95, "SPA":40, "SPD":70, "SPE":110, 
                            "Move1":self.moves["plaquage"], "Move2":self.moves["seisme"],
                            "Move3":self.moves["deflagration"], "Move4":self.moves["psykoud'boul"]}
        }
        
    def initTypeTable(self):
        
        self.types["normal"].setWeaknesses([self.types["combat"]])
        self.types["normal"].setImmunities([self.types["spectre"]])        
        self.types["feu"].setWeaknesses([self.types["eau"],self.types["roche"],self.types["sol"]])
        self.types["feu"].setResistances([self.types["feu"],self.types["insecte"],self.types["plante"],self.types["glace"],self.types["acier"],self.types["fee"]])
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

    def getTypes(self):
        return self.types