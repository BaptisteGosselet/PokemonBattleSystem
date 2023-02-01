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

        substitute = self.opponent.getCurrentPokemon().generateSubstitute()
        print("AITRAINER OK :",substitute.getName())

        my_actions = [
            MoveAction(self.currentPokemon, self.currentPokemon.getMove1()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove2()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove3()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove4()),
        ]

        betterAction = None
        statusActions = []

        maxDamage = 0
        for a in my_actions:
            if(a.getMove().getPower()==0):
                statusActions.append(a)
            else:
                simulation = a.simulate(self.opponent.getCurrentPokemon())
                if(simulation > maxDamage):
                    maxDamage = simulation
                    betterAction = a

        print(betterAction.getMove().getName())
        


        #Est-ce que je tombe K.O. à la prochaine pire attaque ?
            # Je suis full PV ?
                #Switch sur celui qui prends le moins de dégats
                #/(je ne suis pas full pv)
            #/ Je suis celui qui fait le plus de dégat par rapport à l'opposant ?
                # Attaquer avec la plus puissante attaque
                
                #Est-ce que je suis celui qui fait le plus de dégat de mon équipe ?
                    # j'attaque

                    # Est-ce que le meilleur survit au switch ?
                        #switch

                        #j'attaque


       

        if(self.currentPokemon.getIsKo()):
            for i in range(len(self.team)):
                if(not self.team[i].getIsKo()):
                    self.action = SwitchAction(self,i)
                    break
        else:
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        
    def getIsAI(self):
        return True