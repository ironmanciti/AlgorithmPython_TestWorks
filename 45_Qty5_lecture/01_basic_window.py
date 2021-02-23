import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 300, 450)  #(x, y, w, h)
        self.setWindowTitle("This is our Window Title")
        
        self.show()
        
App = QApplication(sys.argv)
window = Window()
App.exec_()
    
    
        
