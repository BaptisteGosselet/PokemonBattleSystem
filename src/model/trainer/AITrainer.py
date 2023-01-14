from model.action.MoveAction import MoveAction
from model.action.SwitchAction import SwitchAction
from model.trainer.Trainer import Trainer

class AITrainer(Trainer) :

    def waitForAction(self, view):
        """
        Choose and generate an action to play
        """
        if(self.currentPokemon.getIsKo()):
            for i in range(len(self.team)):
                if(not self.team[i].getIsKo()):
                    self.action = SwitchAction(self,i)
                    break
        else:
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        
    def getIsAI(self):
        return True