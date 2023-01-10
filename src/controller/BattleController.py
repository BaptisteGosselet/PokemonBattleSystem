from model.Pokemon import Pokemon
from model.PokemonFactory import PokemonFactory
from model.trainer.AITrainer import AITrainer
from model.trainer.Trainer import Trainer


class BattleController() : 

    def __init__(self):
        self.pkFact = PokemonFactory()

    def setView(self, view):
        self.view = view

    def newGame(self):

        self.view.resetGame()

        namesList_p1 = self.view.selectTeam(self.pkFact.getNamesList(), True)
        namesList_p2 = self.view.selectTeam(self.pkFact.getNamesList(), False)

        self.t1 = Trainer("Joueur", [
                    self.pkFact.generatePokemon(namesList_p1[0]), 
                    self.pkFact.generatePokemon(namesList_p1[1]), 
                    self.pkFact.generatePokemon(namesList_p1[2]), 
                ], True)        
                
        self.t2 = AITrainer("Ordinateur", [
                    self.pkFact.generatePokemon(namesList_p2[0]), 
                    self.pkFact.generatePokemon(namesList_p2[1]), 
                    self.pkFact.generatePokemon(namesList_p2[2]), 
                ], False)

        self.view.setOpponentPokemon(self.t2.getCurrentPokemon())
        self.view.setAllyPokemon(self.t1.getCurrentPokemon())
        
        self.play()

    def play(self):
        self.t1.waitForAction(self.view)
        self.t2.waitForAction(self.view)

        if(self.t1.getAction().isFirst(self.t2.getAction())):
            self.t1.getAction().execute(self.view, self.t2.getCurrentPokemon())
            if(not self.t2.getCurrentPokemon().getIsKo()):
                self.t2.getAction().execute(self.view, self.t1.getCurrentPokemon())
        else:
            self.t2.getAction().execute(self.view, self.t1.getCurrentPokemon())
            if(not self.t1.getCurrentPokemon().getIsKo()):
                self.t1.getAction().execute(self.view, self.t2.getCurrentPokemon())


        if(self.t1.getCurrentPokemon().getIsKo()):
            self.t1.waitForAction(self.view)
            self.t1.getAction().execute(self.view, self.t2.getCurrentPokemon())
        if(self.t2.getCurrentPokemon().getIsKo()):
            self.t2.waitForAction(self.view)
            self.t2.getAction().execute(self.view, self.t1.getCurrentPokemon())

        print("fin")