from PyQt5.QtWidgets import *
import sys, os
import sqlite3

con = sqlite3.connect('employees.db')
cur = con.cursor()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("직원 인사 관리")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()
        
    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
        self.displayFirstRecord()
    
    def mainDesign(self):
        #--- Widgets ----------------
        self.employeeList = QListWidget()
        self.btnAdd = QPushButton("추가")
        self.btnDelete = QPushButton("삭제")
        #--- Widget과 function 연결 ----
        self.btnAdd.clicked.connect(self.addEmployee)
        self.btnDelete.clicked.connect(self.deleteEmployee)
        #--- Employee List에 Single Click Event 생성 ----
        self.employeeList.itemClicked.connect(self.singleClick)
    
    def layouts(self):
        #--- Layouts ------------------
        self.mainlayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        #---- Adding child to main Layouts -------
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainlayout.addLayout(self.leftLayout, 40) #aspect ratio
        self.mainlayout.addLayout(self.rightMainLayout, 60)
        #--- adding widgets to layouts --------
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnAdd)
        self.rightBottomLayout.addWidget(self.btnDelete)
        #--- setting main window layout --------
        self.setLayout(self.mainlayout)
        
    def addEmployee(self):
        self.addWindow = AddEmployee()
        self.close()   # Main Window close
        
    def getEmployees(self):
        sql = "SELECT id, name, phone FROM employees"
        result = cur.execute(sql).fetchall()
        for id, name, phone in result:
            self.employeeList.addItem(str(id)+" "+name+" "+phone)
    
    def displayFirstRecord(self):
        sql = "SELECT * FROM employees ORDER BY id ASC LIMIT 1"
        person = cur.execute(sql).fetchone()
        if person:
            self.singleRecord(person)
            
    def singleClick(self):
        #--- clear widgets in layout ---------
        for i in reversed(range(self.leftLayout.count())):
            self.leftLayout.itemAt(i).widget().deleteLater()
            
        employee = self.employeeList.currentItem().text()
        sql = "SELECT * FROM employees WHERE id = ?"
        person = cur.execute(sql, (employee[0],)).fetchone()
        if person:
            self.singleRecord(person)
      
    def singleRecord(self, person):
        #-- person: (id, name, phone)
        name = QLabel(person[1])
        phone = QLabel(person[2])
        
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Phone: ", phone)
        
        
    def deleteEmployee(self):
        if self.employeeList.selectedItems():  # 선택된 item이 있는 경우만 수행
            employee = self.employeeList.currentItem().text()
            mbox = QMessageBox.question(self, "Warning", "정말로 삭제 하시겠습니까 ?",
                                QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                sql = "DELETE FROM employees WHERE id = ?"
                try:
                    cur.execute(sql, (employee[0],))
                    con.commit()
                    QMessageBox.information(self, "Warning", "삭제 완료 하였습니다.")
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.information(self, "Warning", "삭제 실패하였습니다.")
                    con.rollback()
        else:
            QMessageBox.information(self, "Warning", "삭제할 항목을 선택하세요.")
    
#------------------------- Single Employee 추가 등록 --------------------------    
class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.fname = "sample.png"
        self.setWindowTitle("직원 추가")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()
        
    def UI(self):
        self.mainDesign()
        self.layouts()
    
    #--- window가 닫히면 main window 다시 부르기 ----
    def closeEvent(self, event):
        self.main = Main()
    
    def mainDesign(self):
        
        #--- Bottom Layer Widgets -------------
        self.nameLbl = QLabel("성 명: ")
        self.name = QLineEdit()
        self.phoneLbl = QLabel("전화번호: ")
        self.phone = QLineEdit()
        self.addButton = QPushButton("추 가")
        self.addButton.clicked.connect(self.addEmployee)
    
    def layouts(self):
        #--- Layouts ------------------
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        #---- Adding child to main Layouts -------
        self.mainLayout.addLayout(self.topLayout, 40)
        self.mainLayout.addLayout(self.bottomLayout, 60)
        #--- Bottom Layout에 widget 추가 -------
        self.bottomLayout.addRow(self.nameLbl, self.name)
        self.bottomLayout.addRow(self.phoneLbl, self.phone)
        self.bottomLayout.addRow("", self.addButton)
        
        #--- setting sub window layout --------
        self.setLayout(self.mainLayout)
            
    def addEmployee(self):
        name = self.name.text()
        phone = self.phone.text()
    
        if (name and phone):
            try:
                sql = "INSERT INTO employees (name, phone, email, img, address) " +\
                    "VALUES(?, ?, ?, ?, ?)"
                cur.execute(sql, (name, phone, '', '', ''))
                con.commit()
                QMessageBox.information(self, "Success", "새로운 직원 추가 완료")
            except Exception as e:
                print(e)
                QMessageBox.information(self, "Warning", "직원 추가 실패")
        else:
            QMessageBox.information(self, "Warning", "이름과 전화번호는 필수 입력 항목입니다.")
           
def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
