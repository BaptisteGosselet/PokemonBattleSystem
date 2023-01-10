from PyQt5.QtWidgets import *

class TeamLayout(QGridLayout):

    def __init__(self, button_1, button_2):
        super().__init__()            

        self.addItem(QSpacerItem(50,0),0,0)

        self.teamButton_1 = button_1
        self.teamButton_1.setEnabled(False)
        self.teamButton_1.setMinimumSize(150,30)
        self.addWidget(self.teamButton_1,0,1) 

        self.teamButton_2 = button_2
        self.teamButton_2.setEnabled(False)
        self.teamButton_2.setMinimumSize(150,30)
        self.addWidget(self.teamButton_2,1,1) 
        
        self.addItem(QSpacerItem(20,0),0,2)
