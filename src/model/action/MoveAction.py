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

    def execute(self, view, opponentPokemon):
        
        if(random.randint(0,100) <= self.move.getAccuracy()):

            #Dégât au niveau 100
            damage = 42 

            #Puissance multiplié par la stat d'Atk/Def ou de Spa/Spd
            moveIsSpecial = self.move.getIsSpecial()

            if (moveIsSpecial):
                damage *= self.move.getPower() * self.myPokemon.getSpaStat() / opponentPokemon.getSpdStat()
            else:
                damage *= self.move.getPower() * self.myPokemon.getAtkStat() / opponentPokemon.getDefStat()

            damage = damage / 50 + 2

            #Coup critique 
            coupCritique = False
            if(random.randint(0,100) <= 16):
                coupCritique = True
                damage *= 2

            #Roll
            damage *= (random.randint(85,100) / 100)
            
            #STAB
            if(self.move.getType() == self.myPokemon.getType1() or self.move.getType() == self.myPokemon.getType2()):
                damage *= 1.5

            #Faiblesse et resistance de type
            multType = opponentPokemon.getType1().getMultiplicator(self.move.getType())
            if(opponentPokemon.getType2() != None):
                multType *= opponentPokemon.getType2().getMultiplicator(self.move.getType())
            print(self.move.getName(), opponentPokemon.getName(), multType)

            peuEfficace = False
            superEfficace = False
            insensible = False

            if(multType != 1):
                if(multType == 0):
                    insensible = True
                elif(multType == 0.5):
                    peuEfficace = True
                elif(multType == 2):
                    superEfficace = True

            damage *= multType
            
            #Modificateur 3 : port d'objet ect.
            #...

            damage = int(damage)

            opponentPokemon.applyDamage(damage)
            view.playMove_success(self.myPokemon, self.move, opponentPokemon, damage, coupCritique, peuEfficace, superEfficace, insensible)
            
            #effet TODO #si pas ko
        
        else:
            view.playMove_miss(self.myPokemon, self.move, opponentPokemon)
        
        