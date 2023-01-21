class Status():

    def __init__(self):
        self.name = ""
        self.abbreviation = ""

    def getAbbreviation(self) -> str:
        return self.abbreviation

    def canMove(self)->bool:
        """
        Check if the pokemon can attack dispite his status
        """
        return True

    def applyStatus(self, pokemon):
        """
        apply the status' effect to the pokemon
        @param pokemon, the pokemon to apply the status effect
        """
        return

    def canSwitch(self):
        """
        check if the pokemon can switch dispire his status
        """
        return True
    
    def getStatusMessage(self) -> str:
        return ""

    def getFailMessage(self, pokemon) -> str:
        """
        @return a string to display when the pokemon miss his move due to the status
        """
        return ""
