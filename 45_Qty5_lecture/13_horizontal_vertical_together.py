import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Horizontal and Vertical Layouts Together")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        #--- Main Layout ---
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        
        #--- top Layout -----
        cbox = QCheckBox()
        rbtn = QRadioButton()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3") 
        # margin - left, top, right, bottom
        topLayout.setContentsMargins(150, 10, 20, 20) 
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(btn1)
        topLayout.addWidget(btn2)
        topLayout.addWidget(btn3)
        
        #--- Bottom Layout -----
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")
        
        bottomLayout.setContentsMargins(150, 10, 150, 10)
        bottomLayout.addWidget(btn4)
        bottomLayout.addWidget(btn5)
        
        # self.setLayout(hbox)
        self.setLayout(mainLayout)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
