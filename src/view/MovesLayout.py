from PyQt5.QtWidgets import *

class MovesLayout(QGridLayout):

    def __init__(self):
        super().__init__()            
    
        self.addItem(QSpacerItem(20,0),0,0)

        self.button_1 = QPushButton("")
        self.button_1.setEnabled(False)
        self.button_1.clicked.connect(self.onclick_moveButton_1)
        self.button_1.setMinimumSize(150,50)
        self.addWidget(self.button_1,0,1) 

        self.button_2 = QPushButton("")
        self.button_2.setEnabled(False)
        self.button_2.clicked.connect(self.onclick_moveButton_2)
        self.button_2.setMinimumSize(150,50)
        self.addWidget(self.button_2,1,1) 


        self.addItem(QSpacerItem(50,0),0,2)
            
    def setAttacks(self, pokemon):
        self.button_1.setText(pokemon.move1.getName())
        self.button_1.setEnabled(True)
        self.button_2.setText(pokemon.move2.getName())
        self.button_2.setEnabled(True)
        

    def onclick_moveButton_1(self):
        print(self.button_1.text())

    def onclick_moveButton_2(self):
        print(self.button_2.text())
