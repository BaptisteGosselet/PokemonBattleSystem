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

            #Puissance multiplié par la stat d'Atk ou de Spa
            moveIsSpecial = self.move.getIsSpecial()

            if (moveIsSpecial):
                damage *= self.move.getPower() * self.myPokemon.getSpaStat() / 50 / opponentPokemon.getSpdStat()
            else:
                damage *= self.move.getPower() * self.myPokemon.getAtkStat() / 50 / opponentPokemon.getDefStat()

            #Modificateur 1 : brûlure, reflet, météo, ...
            damage += 2

            #Coup critique 
            coupCritique = False
            if(random.randint(0,100) <= 16):
                coupCritique = True
                damage *= 2

            #Modificateur 2 : Port de l'orbe vie ou effet de l'objet métronome
            
            #Roll
            damage *= (random.randint(217,255) * 100) / 255 / 100
            
            #STAB
            #TODO

            #Faiblesses et resistances
            #TODO
            
            #Modificateur 3 : port d'objet ect.

            damage = int(damage)

            opponentPokemon.applyDamage(damage)
            view.playMove_success(self.myPokemon, self.move, opponentPokemon, damage, coupCritique)
            #si peu efficace super efficace

            #effet TODO
            #Pokemon is KO
            if(opponentPokemon.getIsKo):
                pass

        
        else:
            view.playMove_miss(self.myPokemon, self.move, opponentPokemon)
        
        