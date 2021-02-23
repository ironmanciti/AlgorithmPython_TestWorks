import sys
from PyQt5.QtWidgets import * 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo box")
        self.setGeometry(50, 50, 350, 350)
        self.UI()
        
    def UI(self):
        # combo box
        self.combo = QComboBox(self)
        self.combo.move(150, 80)
        # combo box item 추가
        # 1 item 추가
        self.combo.addItem("Python")
        # multiple items 추가
        self.combo.addItems(["Java", "C++", "R"])
        # for loop 이용
        lst = ["apple", "orange", "banana"]
        for item in lst:
            self.combo.addItem(item)
        for n in range(10):
            self.combo.addItem(str(n))
            
        # Radio Button
        self.male = QRadioButton("남성", self)
        self.male.setChecked(True)
        self.female = QRadioButton("여성", self)
        self.male.move(140, 110)
        self.female.move(200, 110)
        
        # buttons
        button = QPushButton("Submit", self)
        button.move(180, 140)
        button.clicked.connect(self.getValues)  # 함수 연결
        self.show()
        
    def getValues(self):
        value = self.combo.currentText()
        
        if self.male.isChecked():
            print(value + " is male !")
        else:
            print(value + "is female")
        
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()
    
    
        
