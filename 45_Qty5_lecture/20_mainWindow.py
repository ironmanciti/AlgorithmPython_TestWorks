import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        QMessageBox.about(self, "메시지", "clicked 되었습니다.")

if __name__ == '__main__':
    App = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(App.exec_())

