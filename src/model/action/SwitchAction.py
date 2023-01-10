import random


class SwitchAction():
    def __init__(self, trainer, indexTeam):
        self.trainer = trainer
        self.indexTeam = indexTeam

    def isFirst(self, action):

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

    def execute(self, view, opponentPokemon):
        view.withdrawAllyPokemon()
        self.trainer.switchPokemon(self.indexTeam)
        view.setAllyPokemon(self.trainer.getCurrentPokemon())