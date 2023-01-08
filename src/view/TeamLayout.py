from PyQt5.QtWidgets import *

class TeamLayout(QGridLayout):

    def __init__(self):
        super().__init__()            
    

        self.buttons = []
        self.addItem(QSpacerItem(50,0),0,0)

        onclick_functions = [self.onclick_pkmButton_1, self.onclick_pkmButton_2, self.onclick_pkmButton_3, self.onclick_pkmButton_4, self.onclick_pkmButton_5, self.onclick_pkmButton_6]
        for i in range(6) :
            teamButton_i = QPushButton("Pokemon")
            teamButton_i.clicked.connect(onclick_functions[i])
            teamButton_i.setMinimumSize(150,30)
            self.addWidget(teamButton_i,i,1) 

        self.addItem(QSpacerItem(20,0),0,2)
            

    def onclick_pkmButton_1(self):
        print("Pokemon 1")

    def onclick_pkmButton_2(self):
        print("Pokemon 2")

    def onclick_pkmButton_3(self):
        print("Pokemon 3")

    def onclick_pkmButton_4(self):
        print("Pokemon 4")

    def onclick_pkmButton_5(self):
        print("Pokemon 5")

    def onclick_pkmButton_6(self):
        print("Pokemon 6")