import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        #--- Vertical Box -----
        vbox = QVBoxLayout()
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")

        vbox.addStretch()
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)
        vbox.addStretch()
        
        self.setLayout(vbox)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
