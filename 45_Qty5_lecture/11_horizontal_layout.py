import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        #--- Horizontal Box -----
        hbox = QHBoxLayout()
        cbox = QCheckBox()
        rbtn = QRadioButton()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        
        # addStretch()로 채워주면 일정한 크기 유지
        hbox.addStretch()
        hbox.addWidget(cbox)
        hbox.addWidget(rbtn)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addStretch()
        
        # self.setLayout(hbox)
        self.setLayout(hbox)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
