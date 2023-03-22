import testUtils

from controller.action.MoveAction import MoveAction
from controller.action.SwitchAction import SwitchAction
from MockTrainer import MockTrainer

def isFirst_2Switch_Test():
    trainer_1, trainer_2 = MockTrainer(), MockTrainer()
    trainer_1.setArbitraryCurrentPokemon(testUtils.genererUnPokemon("pikachu")) #vitesse 50
    trainer_2.setArbitraryCurrentPokemon(testUtils.genererUnPokemon("raichu")) #vitesse 110
    act_1 = SwitchAction(trainer_1, None)
    act_2 = SwitchAction(trainer_2, None)
    return act_2.isFirst(act_1)

def isFirst_Switch_Test():
    act_1 = MoveAction(None, None)
    act_2 = SwitchAction(None, None)
    return act_2.isFirst(act_1)

def isFirst_2Moves_Test():
    pkm_1, pkm_2 = testUtils.genererUnPokemon("pikachu"), testUtils.genererUnPokemon("raichu")
    move = testUtils.genererUnMove()
    act_1 = MoveAction(pkm_1, move) #vitesse 50
    act_2 = MoveAction(pkm_2, move) #vitesse 110
    return act_2.isFirst(act_1)

def isFirst_Priority_Moves_Test():
    pkm_1, pkm_2 = testUtils.genererUnPokemon("pikachu"), testUtils.genererUnPokemon("raichu")
    move_0 = testUtils.genererUnMove()
    move_p = testUtils.genererUnMove(1)
    act_1 = MoveAction(pkm_1, move_p) #vitesse 50
    act_2 = MoveAction(pkm_2, move_0) #vitesse 110
    return not act_2.isFirst(act_1)


def execute_Test():
    mon_poke = testUtils.genererUnPokemon()
    act = MoveAction(testUtils.genererUnPokemon(), testUtils.genererUnMove())
    pv_1 = mon_poke.getCurrentHP()
    act.execute(mon_poke)
    pv_2 = mon_poke.getCurrentHP()
    return pv_1 > pv_2

