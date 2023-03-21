import testUtils

def getPourcentageHP_Test():
    poke = testUtils.genererUnPokemon()
    maxHp = poke.getMaxHP()
    poke.applyDamage(maxHp/2)
    return poke.getPourcentageHP() == 50

def getCurrentHP_Test():
    poke = testUtils.genererUnPokemon()
    maxHp = poke.getMaxHP()
    poke.applyDamage(30)
    expectedHp = maxHp-30
    return poke.getCurrentHP() == expectedHp

def modifAtk_Test():
    poke = testUtils.genererUnPokemon()
    atk_0 = poke.getAtkStat()
    poke.modifAtk(1)
    atk_1 = poke.getAtkStat()
    return atk_1 == (atk_0 + int(atk_0*25/100))

def heal_Test():
    poke = testUtils.genererUnPokemon()
    poke.applyDamage(50)
    poke.heal(30) #-20
    return poke.getCurrentHP() == (poke.getMaxHP() - 20)

def applyDamage_Test():
    poke = testUtils.genererUnPokemon()
    poke.applyDamage(poke.getMaxHP())
    return poke.getIsKo()

def canParalyse_Test():
    poke_normal = testUtils.genererPokemonAvecUnType("normal")
    poke_type = testUtils.genererPokemonAvecUnType("electrik")
    return poke_normal.canParalyse() and (not poke_type.canParalyse())

def canPoison_Test():
    poke_normal = testUtils.genererPokemonAvecUnType("normal")
    poke_type = testUtils.genererPokemonAvecUnType("poison")
    return poke_normal.canPoison() and (not poke_type.canPoison())

def canFreeze_Test():
    poke_normal = testUtils.genererPokemonAvecUnType("normal")
    poke_type = testUtils.genererPokemonAvecUnType("glace")
    return poke_normal.canFreeze() and (not poke_type.canFreeze())
