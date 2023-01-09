from PyQt5.QtWidgets import *

class TeamLayout(QGridLayout):

    def __init__(self):
        super().__init__()            
    

        self.buttons = []
        self.addItem(QSpacerItem(50,0),0,0)

        onclick_functions = [self.onclick_pkmButton_1, self.onclick_pkmButton_2]
        for i in range(2) :
            teamButton_i = QPushButton("Pokemon")
            teamButton_i.clicked.connect(onclick_functions[i])
            teamButton_i.setMinimumSize(150,30)
            self.addWidget(teamButton_i,i,1) 

        self.addItem(QSpacerItem(20,0),0,2)
            

    def onclick_pkmButton_1(self):
        print("Pokemon 1")

    def onclick_pkmButton_2(self):
        print("Pokemon 2")
