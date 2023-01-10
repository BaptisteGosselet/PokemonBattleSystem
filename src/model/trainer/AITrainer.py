from model.action.MoveAction import MoveAction
from model.action.SwitchAction import SwitchAction
from model.trainer.Trainer import Trainer

class AITrainer(Trainer) :

    def waitForAction(self, view):
        #l'ia choisit son action, pour l'instant elle fait toujours sa première attaque
        
        if(self.currentPokemon.getIsKo()):
            self.action = SwitchAction(self,0, self.isAlly)
        else:
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        