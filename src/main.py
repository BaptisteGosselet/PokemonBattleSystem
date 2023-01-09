import sys
from PyQt5.QtWidgets import *

from controller.BattleController import BattleController
from view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    controller = BattleController()
    
    window.setController(controller)
    controller.setView(window)
    
    window.setWindowTitle("Pokemon Battle System")

    window.show()
    sys.exit(app.exec_())