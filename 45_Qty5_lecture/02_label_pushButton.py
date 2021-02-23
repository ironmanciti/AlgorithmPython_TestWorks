import sys
from PyQt5.QtWidgets import * 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()
        
    def UI(self):
        self.text = QLabel("텍스트 입력", self)
        b1 = QPushButton("Enter", self)
        b2 = QPushButton("Exit", self)
        self.text.move(160, 50)
        b1.move(100, 80)
        b2.move(200, 80)
        #--- connect button to function
        b1.clicked.connect(self.b1_func)
        b2.clicked.connect(self.b2_func)
    
        self.show()
        
    def b1_func(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150, 20)
        
    def b2_func(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150, 20)
        
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
    
    
        
