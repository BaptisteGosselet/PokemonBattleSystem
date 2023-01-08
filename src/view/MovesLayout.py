from PyQt5.QtWidgets import *

class MovesLayout(QGridLayout):

    def __init__(self):
        super().__init__()            
    
        self.buttons = []
        self.addItem(QSpacerItem(20,0),0,0)

        onclick_functions = [self.onclick_moveButton_1, self.onclick_moveButton_2, self.onclick_moveButton_3, self.onclick_moveButton_4]
        for i in range(4) :
            moveButton_i = QPushButton("Attaque")
            moveButton_i.clicked.connect(onclick_functions[i])
            moveButton_i.setMinimumSize(150,50)
            self.addWidget(moveButton_i,i,1) 

        self.addItem(QSpacerItem(50,0),0,2)
            

    def onclick_moveButton_1(self):
        print("Attaque 1")

    def onclick_moveButton_2(self):
        print("Attaque 2")

    def onclick_moveButton_3(self):
        print("Attaque 3")

    def onclick_moveButton_4(self):
        print("Attaque 4")