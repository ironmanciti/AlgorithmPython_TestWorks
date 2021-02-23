# record 추가, 삭제 용도로 사용
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer")
        self.setGeometry(50, 50, 500, 500)
        self.UI()

    def UI(self):
        # QLabel with color
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(40, 20)
        # Buttons
        btnStart = QPushButton("Start", self)
        btnStart.move(80, 300)
        btnStart.clicked.connect(self.start)
        btnStop  = QPushButton("Stop", self)
        btnStop.move(190, 300)
        btnStop.clicked.connect(self.stop)
        # connect function to Timer
        self.timer = QTimer()
        self.timer.setInterval(500)  # interval 설정
        self.timer.timeout.connect(self.changeColor)
        self.flip = True
        
        self.show()
        
    def start(self):
        self.timer.start()
        
    def stop(self):
        self.timer.stop()
        
    def changeColor(self):
        if self.flip:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.flip = False
        else:
            self.colorLabel.setStyleSheet("background-color:red")
            self.flip = True

def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()    # window 시작 부터 blink -
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
