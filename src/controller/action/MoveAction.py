import random
from model.Move import Move
from controller.action.SwitchAction import SwitchAction
from model.Pokemon import Pokemon

class MoveAction():
    
    def __init__(self, myPokemon : Pokemon, move : Move):
        self.myPokemon = myPokemon
        self.move = move

        self.target = None
        self.damage = 0

        self.missed = False
        self.statusSetted = False
        self.failByStatus = False
        
        self.immunite = False
        self.coupCritique = False
        self.peuEfficace = False
        self.superEfficace = False

    def getMove(self) -> Move:
        return self.move

    def getMyPokemon(self) -> Pokemon:
        return self.myPokemon

    def getDamage(self) -> int:
        return self.damage

    def getCoupCritique(self) -> bool:
        return self.coupCritique

    def getImmunite(self)->bool:
        return self.immunite

    def getPeuEfficace(self) -> bool:
        return self.peuEfficace

    def getSuperEfficace(self) -> bool:
        return self.superEfficace

    def getTarget(self) -> bool:
        return self.target
    
    def getStatusSetted(self) -> bool:
        return self.statusSetted

    def getFailByStatus(self) -> bool:
        return self.failByStatus

    def getMissed(self) -> bool:
        return self.missed

    def isFirst(self, action) -> bool:
        """
        Compare the order between this action and the action in argument
        @param the action to compare with
        @return true if this action is executable before the action in argument, else false
        """

        if(type(action)==SwitchAction):
            return False

        myMovePrio = self.getMove().getPriority()
        oppMovePrio = action.getMove().getPriority()
        
        if(myMovePrio > oppMovePrio):
            return True
        elif(myMovePrio < oppMovePrio):
            return False
        
        mySpe = self.myPokemon.getSpeStat()
        oppSpe = action.getMyPokemon().getSpeStat()

        if(mySpe > oppSpe):
            return True
        elif(mySpe < oppSpe):
            return False
        else: 
            return bool(random.getrandbits(1))

    def execute(self, opponentPokemon:Pokemon):
        """
        Execute this action : calculate and apply damage and effect of the move
        @param opponentPokemon, the target of the move
        """
        
        self.target = opponentPokemon

        pkmCanMove = True
        if(self.myPokemon.getStatus() != None):
            pkmCanMove = self.myPokemon.getStatus().canMove()

        if(pkmCanMove):

            if(random.randint(0,100) <= self.move.getAccuracy()):

                self.damage = 0
                if(self.move.getPower() != 0):

                    #Dégât au niveau 100
                    self.damage = 42 

                    #Puissance multiplié par la stat d'Atk/Def ou de Spa/Spd
                    moveIsSpecial = self.move.getIsSpecial()

                    if (moveIsSpecial):
                        self.damage *= self.move.getPower() * self.myPokemon.getSpaStat() / opponentPokemon.getSpdStat()
                    else:
                        self.damage *= self.move.getPower() * self.myPokemon.getAtkStat() / opponentPokemon.getDefStat()

                    self.damage = self.damage / 50 + 2

                    #Coup critique 
                    if(random.randint(0,100) <= 6.25):
                        self.coupCritique = True
                        self.damage *= 2

                    #Roll
                    self.damage *= (random.randint(85,100) / 100)
                    
                    #STAB
                    if(self.move.getType() == self.myPokemon.getType1() or self.move.getType() == self.myPokemon.getType2()):
                        self.damage *= 1.5

                    #Faiblesse et resistance de type
                    multType = opponentPokemon.getType1().getMultiplicator(self.move.getType())
                    if(opponentPokemon.getType2() != None):
                        multType *= opponentPokemon.getType2().getMultiplicator(self.move.getType())


                    if(multType == 0):
                        self.immunite = True
                    elif(multType == 0.5):
                        self.peuEfficace = True
                    elif(multType == 2):
                            self.superEfficace = True

                    self.damage *= multType
                    
                    #(Modificateur 3 : port d'objet ect.)
                    
                    self.damage = int(self.damage)

                    opponentPokemon.applyDamage(self.damage)

                if(not opponentPokemon.getIsKo()):
                    if(self.move.getSndEffect() != None):
                        self.statusSetted = self.move.getSndEffect().applyEffect(opponentPokemon)
            
            else:
                self.missed = True

        else:
            self.failByStatus = True

        
        
        
        