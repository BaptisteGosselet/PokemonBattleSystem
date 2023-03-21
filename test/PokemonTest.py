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

def getAtkStat_Test():
    #quand brûlé
    return False

def getSpaStat_Test():
    #quand freeze
    return False

def getSpeStat_Test():
    #quand paralysé
    return False

def applyStatus_Test():
    #si déjà status ne rien faire
    return False

def modifAtk_Test():
    #voir getatk ensuite
    return False

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
    #type electrik
    return False

def canPoison_Test():
    return False

def canFreeze_Test():
    return False
