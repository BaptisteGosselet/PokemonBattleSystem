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
        Select an action to play
        """       
        if(self.currentPokemon.getIsKo()):
            for i in range(len(self.team)):
                if(not self.team[i].getIsKo()):
                    self.action = SwitchAction(self,i) #best switch
                    break
        else:
            self.action = self.findBestPlay()
    
    def findBestPlay(self):
        """
        generate an action to play
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
            
            #L'attaque me mets K.O.
            if(self.currentPokemon.getPourcentageHP() > 50):
                return self.findBestSwitch()
            else:
                if(self.currentPokemon.getSpe() >= self.opponent.getCurrentPokemon().getSpe()):
                    return self.findBestMove(my_moveActions, self.opponent.getCurrentPokemon())
                else:
                    return self.findBestMove(self.filterPriorityMoves(my_moveActions), self.opponent.getCurrentPokemon())

        else:

            #L'attaque ne me mets pas K.O.
            if(myDamage >= oppDamage):
                return self.findBestMove(my_moveActions, self.opponent.getCurrentPokemon())
            else:

               #Est-ce que je suis celui qui fait le plus de dégat de ma team ?
                # Oui -> attaque
                
                # Non -> Est-ce qu'il survit au switch ?
                    #Oui -> Switch
                    #non -> attaque

                
                #voir si je suis celui qui fait le plus de dég de ma team
            

                #non, il y en a un autre 
                #s'il survit au switch -> switch 
                #sinon j'attaque
                
                pass



        return MoveAction(self.currentPokemon, self.currentPokemon.getMove1())

        
    def getIsAI(self):
        return True

    def findBestMove(self, actions, target:Pokemon):
        """
        @param a array of the 4 MoveAction of the launcher and the target
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

    def findBestSwitch(self):
        """
        Find the best choice for switch 
        @return the switch action
        """

        #Check if the switch is possible
        everyoneIsKo = True
        for pkm in self.team:
            everyoneIsKo = everyoneIsKo and pkm.isKo()

        if(everyoneIsKo):
            return self.findBestMove()

        opp_moveActions = [
        MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove1()),
        MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove2()),
        MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove3()),
        MoveAction(self.currentPokemon, self.opponent.getCurrentPokemon().getMove4())
        ]

        total_worseDamage = 0
        index_pkm = None
        for p in len(self.team):
            if(self.team[p].isKo()):
                continue
            else:

                #worse damage that the pokemon can take from the opponent
                p_worseDamage = 0
                for ma in opp_moveActions:
                    simulation = ma.simulate(self.team[p])
                    if(simulation > p_worseDamage):
                        p_worseDamage = simulation

                if(p_worseDamage > total_worseDamage):
                    index_pkm = p
                    total_worseDamage = p_worseDamage
        
        return SwitchAction(self, index_pkm)

    def filterPriorityMoves(self, moveActions:MoveAction):
        """
        Generate a list of priority move actions from a list of "all" move actions
        @param a list of moveActions
        @return the same list with only priority move
        @return (if there is no priority move) the same list of moveActions
        """

        prios = []
        for ma in moveActions:
            if(ma.getMove().getPriority() > 0):
                prios.append(ma)
        
        if(len(prios) > 0):
            return prios
        else:
            return moveActions

    def getPkmIndexOfBestMove(self):
        """
        TODO
        Find the index of the pokemon with the best move in the team (and the current pokemon)
        @return the index of the pokemon on the team (or -1 if it's the current pokemon)
        """

        teamCopy = []
        teamCopy.append(self.currentPokemon)
        teamCopy.append(self.team)

        for pkmIndex in teamCopy:
                
            moveActions = [
                MoveAction(self.currentPokemon, self.currentPokemon.getMove1()),
                MoveAction(self.currentPokemon, self.currentPokemon.getMove2()),
                MoveAction(self.currentPokemon, self.currentPokemon.getMove3()),
                MoveAction(self.currentPokemon, self.currentPokemon.getMove4())
            ]
            
            bestDamage = self.findBestMove(moveActions, self.opponent.getCurrentPokemon()).simulate(self.opponent.getCurrentPokemon())
        pass# return pkm_index -1