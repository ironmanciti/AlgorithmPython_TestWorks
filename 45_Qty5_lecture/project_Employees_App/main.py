from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys, os
import sqlite3
from PIL import Image

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
        self.btnUpdate = QPushButton("갱신")
        self.btnDelete = QPushButton("삭제")
        #--- Widget과 function 연결 ----
        self.btnAdd.clicked.connect(self.addEmployee)
        self.btnDelete.clicked.connect(self.deleteEmployee)
        self.btnUpdate.clicked.connect(self.updateEmployee)
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
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        #--- setting main window layout --------
        self.setLayout(self.mainlayout)
        
    def addEmployee(self):
        self.addWindow = AddEmployee()
        self.close()   # Main Window close
        
    def updateEmployee(self):
        if self.employeeList.selectedItems():
            employee = self.employeeList.currentItem().text()
            id = employee[0]
            self.updateWindow = UpdateEmployeeInfo(id)
            self.close()
        else:
            QMessageBox.information(self, "Warning", "변경할 항목을 선택하세요.")
        
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
        #-- person: (id, name, phone, email, img, address)
        name = QLabel(person[1])
        phone = QLabel(person[2])
        email = QLabel(person[3])
        img = QLabel()
        img.setPixmap(QPixmap("images/{}".format(person[4])))
        address = QLabel(person[5])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Phone: ", phone)
        self.leftLayout.addRow("Email: ", email)
        self.leftLayout.addRow("Address", address)
        
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
        #--- Window Style Sheet -------
        self.setStyleSheet("background-color:white; font-size:12pt;")
        #--- Top Layer Widgets ----------------
        self.title = QLabel("직원 추가")
        self.title.setStyleSheet("font-size: 24pt;")
        self.sampleImg = QLabel()
        self.sampleImg.setPixmap(QPixmap('images/sample.png'))
        #--- Bottom Layer Widgets -------------
        self.nameLbl = QLabel("성 명: ")
        self.name = QLineEdit()
        self.phoneLbl = QLabel("전화번호: ")
        self.phone = QLineEdit()
        self.emailLbl = QLabel("이메일: ")
        self.email = QLineEdit()
        self.imgLbl = QLabel("사 진: ")
        self.imgButton = QPushButton("사진 업로드")
        self.imgButton.setStyleSheet("background-color: orange;font-size: 10pt")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLbl = QLabel("주 소: ")
        self.address = QTextEdit()
        self.addButton = QPushButton("추 가")
        self.addButton.setStyleSheet("background-color: orange;font-size: 10pt")
        self.addButton.clicked.connect(self.addEmployee)
    
    def layouts(self):
        #--- Layouts ------------------
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        #---- Adding child to main Layouts -------
        self.mainLayout.addLayout(self.topLayout, 40)
        self.mainLayout.addLayout(self.bottomLayout, 60)
        #--- Top Layout에 widget 추가 --------
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.sampleImg)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(100, 20, 10, 30) #l,t,r,b
        #--- Bottom Layout에 widget 추가 -------
        self.bottomLayout.addRow(self.nameLbl, self.name)
        self.bottomLayout.addRow(self.phoneLbl, self.phone)
        self.bottomLayout.addRow(self.emailLbl, self.email)
        self.bottomLayout.addRow(self.imgLbl, self.imgButton)
        self.bottomLayout.addRow(self.addressLbl, self.address)
        self.bottomLayout.addRow("", self.addButton)
        
        #--- setting sub window layout --------
        self.setLayout(self.mainLayout)
        
    def uploadImage(self):
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 
                    '사진 업로드', '', 'Image Files (*.jpg, *.png')
        if ok:
            self.fname = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("images/{}".format(self.fname))
            self.sampleImg.setPixmap(QPixmap("images/{}".format(self.fname)))
        else:
            QMessageBox.information(self, "Warning", "사진 업로드 실패")
            
    def addEmployee(self):
        name = self.name.text()
        phone = self.phone.text()
        email = self.email.text()
        img = self.fname
        address = self.address.toPlainText()
        if (name and phone):
            try:
                sql = "INSERT INTO employees (name, phone, email, img, address) " +\
                    "VALUES(?, ?, ?, ?, ?)"
                cur.execute(sql, (name, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, "Success", "새로운 직원 추가 완료")
            except Exception as e:
                print(e)
                QMessageBox.information(self, "Warning", "직원 추가 실패")
        else:
            QMessageBox.information(self, "Warning", "이름과 전화번호는 필수 입력 항목입니다.")

#------------------------- Employee Update --------------------------
class UpdateEmployeeInfo(AddEmployee):
    
    def __init__(self, id):
        self.id = id
        super().__init__()
        
    def mainDesign(self):
        sql = "SELECT * from employees WHERE id = ?"
        person = cur.execute(sql, (self.id,)).fetchone()
        #-- person: (id, name, phone, email, img, address)
        #--- Window Style Sheet -------
        self.setStyleSheet("background-color:white; font-size:12pt;")
        #--- Top Layer Widgets ----------------
        self.title = QLabel("직원 정보 변경")
        self.title.setStyleSheet("font-size: 24pt;")
        self.sampleImg = QLabel()
        self.sampleImg.setPixmap(QPixmap("images/{}".format(person[4])))
        #--- Bottom Layer Widgets -------------
        self.nameLbl = QLabel("성 명: ")
        self.name = QLineEdit()
        self.name.setText(person[1])
        self.phoneLbl = QLabel("전화번호: ")
        self.phone = QLineEdit()
        self.phone.setText(person[2])
        self.emailLbl = QLabel("이메일: ")
        self.email = QLineEdit()
        self.email.setText(person[3])
        self.imgLbl = QLabel("사 진: ")  
        self.imgButton = QPushButton("사진 업로드")
        self.imgButton.setStyleSheet(
            "background-color: orange;font-size: 10pt")
        self.imgButton.clicked.connect(self.uploadImage)
        self.addressLbl = QLabel("주 소: ")
        self.address = QTextEdit(person[5])
        self.addButton = QPushButton("갱 신")
        self.addButton.setStyleSheet(
            "background-color: orange;font-size: 10pt")
        self.addButton.clicked.connect(self.updateEmployee)
        
    def updateEmployee(self):
        name = self.name.text()
        phone = self.phone.text()
        email = self.email.text()
        img = self.fname
        address = self.address.toPlainText()
        if (name and phone):
            try:
                sql = "UPDATE employees SET name=?, " +\
                    "phone=?, email=?, img=?, address=? " +\
                    "WHERE id=?"
                cur.execute(sql, (name, phone, email, img, address, self.id))
                con.commit()
                QMessageBox.information(self, "Success", "직원 정보 변경 완료")
            except Exception as e:
                print(e)
                QMessageBox.information(self, "Warning", "직원 정보 변경 실패")
                con.rollback()
        else:
            QMessageBox.information(self, "Warning", "이름과 전화번호는 필수 입력 항목입니다.")
           
def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
