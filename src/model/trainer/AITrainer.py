from controller.action.MoveAction import MoveAction
from controller.action.SwitchAction import SwitchAction
from model.trainer.Trainer import Trainer

class AITrainer(Trainer) :

    def setOpponent(self, opp):
        """
        setter for the opponent player
        """
        self.opponent = opp

    def waitForAction(self, view):
        """
        Choose and generate an action to play
        """

        print("AITRAINER OK :",self.opponent.getName())

        if(self.currentPokemon.getIsKo()):
            for i in range(len(self.team)):
                if(not self.team[i].getIsKo()):
                    self.action = SwitchAction(self,i)
                    break
        else:
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        
    def getIsAI(self):
        return True