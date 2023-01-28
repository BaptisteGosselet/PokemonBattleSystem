from random import randint
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class TrainerGeneratorPopup(QDialog):
    
    def __init__(self, saisieNom_J1, saisieNom_J2, caseAI, combos_J1, combos_J2):
        super().__init__()

        self.combos_J1 = combos_J1
        self.combos_J2 = combos_J2

        self.setWindowTitle("Pokemon Battle System")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setMinimumSize(800,200)

        globalLayout = QGridLayout()
        saisieNom_J1.setMaximumSize(200,50)
        saisieNom_J2.setMaximumSize(200,50)
        globalLayout.addWidget(saisieNom_J1, 0, 0)
        globalLayout.addWidget(saisieNom_J2, 0, 1)

        globalLayout.addWidget(caseAI, 0, 3)

        choice_layout_J1 = QVBoxLayout()
        choice_layout_J2 = QVBoxLayout()
        for i in range(len(combos_J1)):
            choice_layout_J1.addWidget(combos_J1[i])
            choice_layout_J2.addWidget(combos_J2[i])
        
        shuffle_button_1 = QPushButton("Aléatoire")
        shuffle_button_1.clicked.connect(self.onClick_rand1)
        choice_layout_J1.addWidget(shuffle_button_1)

        shuffle_button_2 = QPushButton("Aléatoire")
        shuffle_button_2.clicked.connect(self.onClick_rand2)
        choice_layout_J2.addWidget(shuffle_button_2)


        globalLayout.addLayout(choice_layout_J1, 2, 0)
        globalLayout.addLayout(choice_layout_J2, 2, 1)

        ok_button = QPushButton("Valider")
        ok_button.clicked.connect(self.onClick_ok)
        globalLayout.addWidget(ok_button, 3, 3)

        self.setLayout(globalLayout)

        self.onClick_rand1()
        self.onClick_rand2()

        self.exec()

    def onClick_rand1(self):
        for combo in self.combos_J1:
            combo.setCurrentIndex(randint(0,combo.count()-1))

    def onClick_rand2(self):
        for combo in self.combos_J2:
            combo.setCurrentIndex(randint(0,combo.count()-1))


    def onClick_ok(self):
        self.close()