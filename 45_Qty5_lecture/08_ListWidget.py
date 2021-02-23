# record 추가, 삭제 용도로 사용
import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List Widget")
        self.setGeometry(50, 50, 500, 500)
        self.UI()
        
    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        # List Widget
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)
        # add items to List Widget
        lst = ['Python', 'C++', 'Java']
        self.listWidget.addItems(lst)
        # add one item
        self.listWidget.addItem('JavaScript')
        # add using for
        for n in range(1, 3):
            self.listWidget.addItem(str(n))
        #-----------------------------------
        # button 추가
        btnAdd = QPushButton("Add", self)
        btnAdd.move(360, 80)
        btnDelete = QPushButton("Delete", self)
        btnDelete.move(360, 110)
        btnGet = QPushButton("Get", self)
        btnGet.move(360, 140)
        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.move(360, 170)
        # function connect
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)
        
        self.show()
        
    def funcAdd(self):
        val = self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")
        
    def funcDelete(self):
        idx = self.listWidget.currentRow()
        self.listWidget.takeItem(idx)  # delete from List Widget
    
    def funcGet(self):
        val = self.listWidget.currentItem().text()
        print(val)
        
    def funcDeleteAll(self):
        self.listWidget.clear()   # delete all
    
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()