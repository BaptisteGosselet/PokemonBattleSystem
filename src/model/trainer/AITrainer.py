from controller.action.MoveAction import MoveAction
from controller.action.SwitchAction import SwitchAction
from model.Pokemon import Pokemon
from model.trainer.Trainer import Trainer
from random import choice

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

        my_moveActions = [
            MoveAction(self.currentPokemon, self.currentPokemon.getMove1()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove2()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove3()),
            MoveAction(self.currentPokemon, self.currentPokemon.getMove4())
        ]

        opp_moveActions = [
            MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove1()),
            MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove2()),
            MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove3()),
            MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove4())
        ]

        myBestMove = self.findBestMove(my_moveActions, self.opponent.getCurrentPokemon())
        oppBestMove = self.findBestMove(opp_moveActions, self.currentPokemon)
        
        myDamage = oppBestMove.simulate(self.currentPokemon)
        oppDamage = myBestMove.simulate(self.opponent.getCurrentPokemon())

        if(myDamage >= self.currentPokemon.getCurrentHP()):
            #Je K.O.
            if(self.currentPokemon.getPourcentageHP() == 100):
                pass
                #Je full pv
            else:
                pass
                #j'ai déjà pris des dommages



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

    def findBestMove(self, actions, target:Pokemon):
        """
        @param a array of the 4 MoveAction of the launcher
        @return the best move to do 
        """
        betterAction = None
        statusActions = []

        maxDamage = 0
        for a in actions:
            if(a.getMove().getPower()==0):
                statusActions.append(a)
            else:
                simulation = a.simulate(target)
                if(simulation > maxDamage):
                    maxDamage = simulation
                    betterAction = a

        if((len(statusActions) > 1) and
            target.getCurrentHP()/2 > maxDamage and target.getStatus() == None
            or betterAction == None): 
            
            betterAction = choice(statusActions)

        return betterAction