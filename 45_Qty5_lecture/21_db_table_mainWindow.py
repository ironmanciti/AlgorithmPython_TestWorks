import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3

#from PyQt5.uic.properties import QtWidgets

#--------------- test db 생성 ----------------------------
con = sqlite3.connect('emaildb.db')
cur = con.cursor()
try:
    cur.execute("DROP TABLE IF EXISTS emails")
    cur.execute("CREATE TABLE emails (email TEXT, weekday TEXT, month TEXT, day TEXT)")
    print('table created successfully')
except Exception as e:
    print('error in operation, ', e)
    con.rollback()
    con.close()
    
fname = 'emailbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    weekday = pieces[2]
    month = pieces[3]
    day = pieces[4]
    
    cur.execute('INSERT INTO emails (email, weekday, month, day) VALUES (?, ?, ?, ?)',
                    (email, weekday, month, day))
    con.commit()

#--------------- window 시작 -----------------------
form_class = uic.loadUiType("21_db_table.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn_load.clicked.connect(self.loadData)
        
    def loadData(self):
        query = "SELECT * FROM emails"
        result = cur.execute(query)
        self.tableWidget.setRowCount(0)

        for row_idx, row in enumerate(result):
            self.tableWidget.insertRow(row_idx)
            for col_idx, col in enumerate(row):
                self.tableWidget.setItem(row_idx, col_idx,
                                QTableWidgetItem(col))
                
        con.close()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(App.exec_())

