from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FDTD Simulation")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()        