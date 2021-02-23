import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box")
        self.setGeometry(250, 150, 500, 500)
        self.UI()
        
    def UI(self):
        button = QPushButton("Click Me", self)
        button.setFont(font)
        button.move(200, 150)
        # Message Box display
        button.clicked.connect(self.message_spin_Box)
       
        self.show()
        
    def message_spin_Box(self):
        # Message Box
        mbox = QMessageBox.question(self, "Warning !!", 
                "Are you sure to quit ?", 
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
        else:
            print("Click Me is working")
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
