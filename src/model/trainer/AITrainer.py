from model.action.MoveAction import MoveAction
from model.trainer.Trainer import Trainer

class AITrainer(Trainer) :

    def waitForAction(self, view):
        #l'ia choisit son action, pour l'instant elle fait toujours sa première attaque
        self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        