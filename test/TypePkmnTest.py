import testUtils

def getMultiplicatorTest_2():
    sol, electrik = testUtils.genererTypes_sol_electrik()
    return electrik.getMultiplicator(sol) == 2
    
def getMultiplicatorTest_05():
    sol, electrik = testUtils.genererTypes_sol_electrik()
    return electrik.getMultiplicator(electrik) == 0.5

def getMultiplicatorTest_0():
    sol, electrik = testUtils.genererTypes_sol_electrik()
    return sol.getMultiplicator(electrik) == 0
