from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class SelectPopup(QDialog):
    def __init__(self, statusBar, combo_1, combo_2, combo_3):
        super().__init__()

        self.setWindowTitle("Pokemon Battle System")

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.setMinimumSize(400,200)

        ok_button = QPushButton("Valider")
        ok_button.clicked.connect(self.onClick_ok)

        layout = QVBoxLayout()
        layout.addWidget(statusBar)
        layout.addWidget(combo_1)
        layout.addWidget(combo_2)
        layout.addWidget(combo_3)
        layout.addWidget(ok_button)

        self.setLayout(layout)

        self.exec()

    def onClick_ok(self):
        self.close()