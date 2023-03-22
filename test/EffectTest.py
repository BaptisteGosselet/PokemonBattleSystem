import testUtils

from model.effect.HealAndRecoilEffect import HealAndRecoilEffect
from model.effect.StatChangeEffect import StatChangeEffect
from model.effect.StatusEffect import StatusEffect


def healAndRecoil_Test():
    poke = testUtils.genererUnPokemon()
    poke.applyDamage(poke.getCurrentHP()//2) #-50%
    e = HealAndRecoilEffect(30, True) #+30%
    e.applyEffect(poke)
    return poke.getPourcentageHP() == 80
    
def statChange_Test():
    poke = testUtils.genererUnPokemon()
    e = StatChangeEffect([1,0,0,0,0], 100, False)
    atk_1 = poke.getAtkStat()
    e.applyEffect(poke)
    atk_2 = poke.getAtkStat()
    return atk_2 == atk_1 + int(25/100*atk_1)

def statusEffect_Test():
    poke = testUtils.genererPokemonAvecUnType("normal")
    para, pois = testUtils.genererParalysieEtPoison()
    e1 = StatusEffect(para, 100, False)
    e2 = StatusEffect(pois, 100, False)
    b1 = e1.applyEffect(poke)
    b2 = e2.applyEffect(poke)
    return b1 and (not b2)
