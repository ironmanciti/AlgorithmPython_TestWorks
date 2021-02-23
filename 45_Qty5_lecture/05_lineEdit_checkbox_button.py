import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Images")
        self.setGeometry(50, 50, 500, 400)
        self.UI()
        
    def UI(self):
        # input field
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("이름을 입력하세요")
        self.name.move(150, 80)
        # check box
        self.check = QCheckBox("이름 기억", self)
        self.check.move(150, 110)
        # button
        button = QPushButton("submit", self)
        button.move(200, 140)
        button.clicked.connect(self.submit)
        self.show()
    
    def submit(self):
        if self.check.isChecked():
            print("Name : ", self.name.text(), "checkbox checked !!")
        else:
            print("Name : ", self.name.text(), "checkbox NOT checked !!")
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
