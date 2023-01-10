from PyQt5.QtWidgets import *

class MovesLayout(QGridLayout):

    def __init__(self, button_1, button_2):
        super().__init__()            
    
        self.addItem(QSpacerItem(20,0),0,0)

        self.button_1 = button_1
        self.button_1.setEnabled(False)
        
        self.button_1.setMinimumSize(150,50)
        self.addWidget(self.button_1,0,1) 

        self.button_2 = button_2
        self.button_2.setEnabled(False)
        self.button_2.setMinimumSize(150,50)
        self.addWidget(self.button_2,1,1) 

        self.addItem(QSpacerItem(50,0),0,2)
