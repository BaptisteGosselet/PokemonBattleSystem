import random

class SwitchAction():

    def __init__(self, trainer, indexTeam : int):
        self.trainer = trainer
        self.indexTeam = indexTeam

    def isFirst(self, action) -> bool:
        """
        Compare the order between this action and the action in argument
        @return true if this action is executable before the action in argument, else false
        """

        if(type(action)==SwitchAction):
            
            mySpe = self.trainer.getCurrentPokemon().getSpeStat()
            oppSpe = action.getPokemon().getSpeStat()
            
            if(mySpe > oppSpe):
                return True
            elif(mySpe < oppSpe):
                return False
            else: 
                return bool(random.getrandbits(1))

        else:
            return True

    def execute(self, opponentPokemon) -> None:
        """
        Execute this action : do the switch of pokemon
        """
        self.trainer.switchPokemon(self.indexTeam)
        