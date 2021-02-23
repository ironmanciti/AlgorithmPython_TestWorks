import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        formLayout = QFormLayout()
        
        name_txt = QLabel("Name: ")
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())
        
        pswd_txt = QLabel("Password: ")
        pswd_input = QLineEdit()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(QPushButton("Enter"))
        hbox2.addWidget(QPushButton("Exit"))
        hbox2.addStretch()
        
        formLayout.addRow(name_txt, hbox1)
        formLayout.addRow(pswd_txt, pswd_input)
        formLayout.addRow(QLabel("Country: "), QComboBox())
        formLayout.addRow(hbox2)
        
        self.setLayout(formLayout)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
