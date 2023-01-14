from model.PokemonFactory import PokemonFactory

class BattleController() : 

    def __init__(self):
        self.pkFact = PokemonFactory()

    def setView(self, view):
        self.view = view

    def newGame(self):

        self.view.resetGame()

        trainers = self.view.generateTrainers(self.pkFact)

        self.t1 = trainers[0]
        self.t2 = trainers[1]

        self.t1.sendCurrentPokemon()
        self.t2.sendCurrentPokemon()
        
        self.play()

    def play(self):
        """
        Play the main loop of the pokemon's game
        """

        gameContinue = True
        while(gameContinue):

            #Main loop
            self.t1.waitForAction(self.view)
            self.t2.waitForAction(self.view)

            if(self.t1.getAction().isFirst(self.t2.getAction())):
                self.t1.getAction().execute(self.t2.getCurrentPokemon())
                self.view.playMove(self.t1.getAction())
                if(not self.t2.getCurrentPokemon().getIsKo()):
                    self.t2.getAction().execute(self.t1.getCurrentPokemon())
                    self.view.playMove(self.t2.getAction())

            else:
                self.t2.getAction().execute(self.t1.getCurrentPokemon())
                self.view.playMove(self.t2.getAction())
                if(not self.t1.getCurrentPokemon().getIsKo()):
                    self.t1.getAction().execute(self.t2.getCurrentPokemon())
                    self.view.playMove(self.t1.getAction())



            #When trainer 1's pokemon is ko
            if(self.t1.getCurrentPokemon().getIsKo()):
                if(not self.t1.canContinue()):
                    self.view.displayWinner(self.t2)
                    break
                else:
                    self.t1.waitForAction(self.view)
                    self.t1.getAction().execute(self.t2.getCurrentPokemon())
                    self.view.playMove(self.t1.getAction())

            #When trainer 2's pokemon is ko
            if(self.t2.getCurrentPokemon().getIsKo()):
                if(not self.t2.canContinue()):
                    self.view.displayWinner(self.t1)
                    break
                else:
                    self.t2.waitForAction(self.view)
                    self.t2.getAction().execute(self.t1.getCurrentPokemon())
                    self.view.playMove(self.t2.getAction())


