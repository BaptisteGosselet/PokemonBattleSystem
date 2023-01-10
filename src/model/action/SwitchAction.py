import random


class SwitchAction():
    def __init__(self, myPokemon, indexTeam):
        self.myPokemon = myPokemon
        self.indexTeam = indexTeam

    def isFirst(self, action):

        if(type(action)==SwitchAction):
            
            mySpe = self.myPokemon.getSpeStat()
            oppSpe = action.getPokemon().getSpeStat()
            
            if(mySpe > oppSpe):
                return True
            elif(mySpe < oppSpe):
                return False
            else: 
                return bool(random.getrandbits(1))

        else:
            return True

    def execute(self):
        print("TODO Switch", self.myPokemon.getName(), self.indexTeam)