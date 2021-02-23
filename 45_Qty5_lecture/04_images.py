import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Images")
        self.setGeometry(50, 50, 800, 500)
        self.UI()
        
    def UI(self):
        # Image display
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('dog.jpg'))
        self.image.move(150, 50)
        # button 눌러서 image 감추기/보이기
        closeButton = QPushButton("이미지 감추기", self)
        closeButton.move(270, 430)
        closeButton.clicked.connect(self.closeImg)
        
        showButton = QPushButton("이미지 보이기", self)
        showButton.move(420, 430)
        showButton.clicked.connect(self.showImg)
        self.show()
        
    def closeImg(self):
        self.image.close()
        
    def showImg(self):
        self.image.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
