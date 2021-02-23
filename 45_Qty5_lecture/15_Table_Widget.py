import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("선택한 item 값 가져오기")
        #--- table size / header 정의 -------
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("성"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("이름"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("주소"))
        #--- table item 값 채우기 ------
        self.table.setItem(0, 0, QTableWidgetItem("오"))
        self.table.setItem(0, 1, QTableWidgetItem("영제"))
        self.table.setItem(0, 2, QTableWidgetItem("서울시"))
        self.table.setItem(4, 2, QTableWidgetItem("경기도"))
        #--- table cell 내용 수정 금지 -----
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #--- table cell double click event trigger ----
        self.table.doubleClicked.connect(self.doubleClicked)
        
        btn.clicked.connect(self.getValue)
        
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        self.show()
        
    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())
            
    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
