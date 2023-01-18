from model.Pokemon import Pokemon
from model.action.MoveAction import MoveAction
from model.action.SwitchAction import SwitchAction
from view.PokemonLayout import PokemonLayout


class Trainer() :

    def __init__(self, name, pokemons, displayer : PokemonLayout):
        self.name = name
        self.displayer = displayer
        self.currentPokemon = pokemons[0]
        self.currentPokemon.setTrainer(self)
        self.team = []
        for i in range(1,len(pokemons)):
            pokemons[i].setTrainer(self)
            self.team.append(pokemons[i])
        self.action = None
        self.actionCommand = None

    def getName(self) -> str:
        return self.name

    def setCurrentPokemon(self, pokemon):
        self.currentPokemon = pokemon
        self.currentPokemon.setTrainer(self)
        self.displayer.setPokemon_noMessage(self.currentPokemon)
        self.displayer.refresh()

    def getCurrentPokemon(self) -> Pokemon :
        return self.currentPokemon

    def getTeam(self) -> list[Pokemon]:
        return self.team

    def setActionCommand(self, command:str) -> None:
        """
        Set an action command (from the MainWindow)
        @param the command
        """

        self.actionCommand = command

    def waitForAction(self, view) -> None:
        """
        Ask an action command from the player and generate the corresponding action
        @param the view
        """
        view.waitForAction(self)

        if(self.actionCommand == "move_1"):
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        elif(self.actionCommand == "move_2"):
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove2())
        elif(self.actionCommand == "switch_1"):
            self.action = SwitchAction(self, 0)
        elif(self.actionCommand == "switch_2"):
            self.action = SwitchAction(self, 1)
        else:
            print("Erreur")

    def getAction(self):
        return self.action

    def getIsAI(self) -> bool:
        """
        @return if this trainer is controlled by a AI (true) or a human (false)
        """
        return False

    def switchPokemon(self, indexTeam : int) -> None:
        """
        Switch the current pokemon with a pokemon from the team
        @param : index of the team's pokemon
        """
        leavingPokemon = self.currentPokemon
        self.currentPokemon = self.team[indexTeam]
        self.team[indexTeam] = leavingPokemon
        self.withdrawPokemon()
        self.sendCurrentPokemon()

    def sendCurrentPokemon(self):
        """
        Call the method from the displayer to display the current pokemon
        """
        self.displayer.setPokemon(self.currentPokemon)

    def withdrawPokemon(self):
        """
        Call the displayer to withdraw the pokemon from the screen
        """

        self.displayer.withdrawPokemon()


    def canContinue(self) -> bool:
        """
        Check if the trainer can continue the game
        @return if there is at least one pokemon left
        """
        if(self.currentPokemon.getIsKo()):
            for pkm in self.team:
                if (not pkm.getIsKo()):
                    return True
            return False
        else:
            return False