import sys
from PyQt5.QtWidgets import *

#QMainWindow 는 menu, toolbar 용도의 window
class Window(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        #--- main menu ----------
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        help = menubar.addMenu("Help")
        #--- sub menu ----------
        new = QAction("New Project", self)
        file.addAction(new)
        open = QAction("Open Project", self)
        file.addAction(open)
        exit = QAction("Exit", self)
        file.addAction(exit)
        #--- menu click event -----
        exit.triggered.connect(self.exitFunc)
        
        self.show()
        
    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", '정말로 끝내시겠습니까 ?', 
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
        
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
