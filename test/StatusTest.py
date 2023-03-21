import testUtils

from model.status.BurnStatus import BurnStatus
from model.status.ParalysisStatus import ParalysisStatus
from model.status.PoisonStatus import PoisonStatus
from model.status.FreezeStatus import FreezeStatus
from model.status.FlinchStatus import FlinchStatus
from model.status.RechargeStatus import RechargeStatus
from model.status.SleepStatus import SleepStatus

def burn_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    atk_1 = poke.getAtkStat()
    poke.setStatus(BurnStatus())
    atk_2 = poke.getAtkStat()
    b1 = atk_1//2 == atk_2
    pv_1 = poke.getCurrentHP()
    poke.applyStatus()
    pv_2 = poke.getCurrentHP()
    b2 = pv_1 > pv_2
    return b1 and b2

def poison_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    poke.setStatus(PoisonStatus())
    pv_1 = poke.getCurrentHP()
    poke.applyStatus()
    pv_2 = poke.getCurrentHP()
    poke.applyStatus()
    pv_3 = poke.getCurrentHP()
    b1 = (pv_1 > pv_2) and (pv_2 > pv_3) #dégât
    b2 = (pv_1 - pv_2) <  (pv_2 - pv_3) #dégâts progressifs
    return b1 and b2

def paralysis_Test():    
    poke = testUtils.genererPokemonAvecUnType("normal")
    vit_1 = poke.getSpeStat()
    poke.setStatus(ParalysisStatus())
    vit_2 = poke.getSpeStat()
    return vit_1//2 == vit_2

def freeze_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    atk_1 = poke.getSpaStat()
    poke.setStatus(FreezeStatus())
    atk_2 = poke.getSpaStat()
    b1 = atk_1//2 == atk_2
    pv_1 = poke.getCurrentHP()
    poke.applyStatus()
    pv_2 = poke.getCurrentHP()
    b2 = pv_1 > pv_2
    return b1 and b2

def flinch_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    poke.setStatus(FlinchStatus())
    poke.applyStatus()
    poke.applyStatus()
    return poke.getStatus() == None

def recharge_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    poke.setStatus(RechargeStatus())
    poke.applyStatus()
    poke.applyStatus()
    return poke.getStatus() == None

def sleep_Test():
    poke = testUtils.genererUnPokemon()
    status = SleepStatus()
    poke.setStatus(status)
    cpt = 0
    while(poke.getStatus()==status):
        cpt += 1
        poke.applyStatus()
    return (cpt > 1) and (cpt <= 5)
