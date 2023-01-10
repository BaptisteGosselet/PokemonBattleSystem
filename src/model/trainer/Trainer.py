from model.action.MoveAction import MoveAction
from model.action.SwitchAction import SwitchAction


class Trainer() :

    def __init__(self, name, pokemons, isAlly):
        self.name = name
        self.isAlly = isAlly
        self.currentPokemon = pokemons[0]
        self.team = []
        for i in range(1,len(pokemons)):
            self.team.append(pokemons[i])

    def getCurrentPokemon(self):
        return self.currentPokemon


    def getTeam(self):
        return self.team

    def setActionCommand(self, command):
        self.actionCommand = command

    def waitForAction(self, view):
        view.waitForAction(self)

        if(self.actionCommand == "move_1"):
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove1())
        elif(self.actionCommand == "move_2"):
            self.action = MoveAction(self.currentPokemon, self.currentPokemon.getMove2())
        elif(self.actionCommand == "switch_1"):
            self.action = SwitchAction(self, 0, self.isAlly)
        elif(self.actionCommand == "switch_2"):
            self.action = SwitchAction(self, 1, self.isAlly)
        else:
            print("Erreur")

    def getAction(self):
        return self.action

    def switchPokemon(self, indexTeam):
        leavingPokemon = self.currentPokemon
        self.currentPokemon = self.team[indexTeam]
        self.team[indexTeam] = leavingPokemon

    def canContinue(self):
        if(self.currentPokemon.getIsKo()):
            for pkm in self.team:
                if (not pkm.getIsKo()):
                    return True
            return False
        else:
            return False