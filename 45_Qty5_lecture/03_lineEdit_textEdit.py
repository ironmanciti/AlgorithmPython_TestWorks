import sys
from PyQt5.QtWidgets import * 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdits")
        self.setGeometry(50, 50, 500, 500)
        self.UI()
        
    def UI(self):
        # input fields 
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("이름을 입력하세요.")
        self.name.move(120, 50)
        self.pswd = QLineEdit(self)
        self.pswd.setPlaceholderText("비밀번호를 입력하세요.")
        self.pswd.setEchoMode(QLineEdit.Password)  #비밀번호 감추기
        self.pswd.move(120, 80)
        
        # text input field
        self.edit = QTextEdit(self)
        self.edit.move(120, 110)
        self.edit.setAcceptRichText(False) # plain text 만 허용
        self.edit.resize(300, 50)
        
        # buttons
        button = QPushButton("Save", self)
        button.move(180, 310)
        button.clicked.connect(self.getValues)  # 함수 연결
        self.show()
        
    def getValues(self):
        name = self.name.text()
        password = self.pswd.text()
        self.setWindowTitle("Your name: " + name + " Password: " + password)
        
        print(self.edit.toPlainText())  # rich text 입력시 plain text 전환
        
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())
    
if __name__ == '__main__':
    main()