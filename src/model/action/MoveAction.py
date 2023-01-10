import random
from model.action.SwitchAction import SwitchAction


class MoveAction():
    
    def __init__(self, myPokemon, move):
        self.myPokemon = myPokemon
        self.move = move

    def getMove(self):
        return self.move

    def getPokemon(self):
        return self.myPokemon

    def isFirst(self, action):

        if(type(action)==SwitchAction):
            return False

        myMovePrio = self.getMove().getPriority()
        oppMovePrio = action.getMove().getPriority()
        
        if(myMovePrio > oppMovePrio):
            return True
        elif(myMovePrio < oppMovePrio):
            return False
        
        mySpe = self.myPokemon.getSpeStat()
        oppSpe = action.getPokemon().getSpeStat()

        if(mySpe > oppSpe):
            return True
        elif(mySpe < oppSpe):
            return False
        else: 
            return bool(random.getrandbits(1))

    def execute(self):
        print("TODO Move", self.myPokemon.getName(), self.move.getName())

        
        