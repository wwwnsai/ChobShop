import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from .Login import *
# from Login import *
# from app.signuptest.Signuprun import *
from app.db.database import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("""
            /* Central widget styling */
            QWidget#centralwidget {
                background-color: #FAF9F6;
            }
                           
            QWidget#leftcontainer {
                background-color: #FAF9F6;
            }
                           
            QWidget#rightcontainer {
                background-color: #E1E3E7;
                margin-left: 27px;
                border-radius: 25px;
            }

            /* Label styling */
            QLabel#loginlabel {
                color: #000;
                font-family: Inter;
                font-size: 48px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            }
                           
            QLabel#noacclabel {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 20px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 100px;
            }
                           
            QPushButton#signfornoaccbutton {
                border: none;
                color: #AEC289;
                font-family: Inter;
                font-size: 20px;
                font-style: bold;
                font-weight: 700;
                border: none;
                line-height: normal;
                margin-right: 400px;
            }
                           
            QPushButton#signfornoaccbutton:hover {
                color: #CD4662;
            }
            
            QLabel#adminlabel {
                color: #CD4662;
                text-align: center;
                font-family: Inter;
                font-size: 18px;
                font-style: normal;
                font-weight: 400;
                line-height: normal;
                margin-left: 310px;
            }

            /* Push button styling */
            QPushButton#loginbutton {
                background-color: #CD4662;
                color: #FFF;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                border-radius: 25px;
            }

            QPushButton#loginbutton:hover {
                background-color: #AEC289;
            }

            /* LineEdit styling */
            QLineEdit#username {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
            
            QLineEdit#password {
                font-size: 24px;
                width: 500px;
                height: 80px;
                border: none;
                border-bottom: 3px solid #000;
                background-color: #FAF9F6;
            }
                           
            QCheckBox#checkbox {
                color: #CD4662;
            }
                           
            QCheckBox#checkbox::indicator {
                border-radius: 3px;
                background-color: #F4DBDB;
                width: 26px;
                height: 26px;
                border: none;
            }

            QCheckBox#checkbox::indicator:checked {
                background-color: #CD4662;
            }
            QCheckBox#checkbox::indicator:unchecked {
                background-color: #F4DBDB;
            }
                           
            QPushButton#home {
               color: #CD4662;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 500;
                line-height: normal;
                border: none;
            }
            QPushButton#home:hover {
               color: #AEC289;
            }

        """)
        
        self.display_image()
        self.ui.loginbutton.clicked.connect(self.login_window) # login button clicked
        self.ui.signfornoaccbutton.clicked.connect(self.open_signup_window) # login button clicked
        self.ui.home.clicked.connect(self.go_to_homepage)

    def display_image(self):
        image_path = "app/assets/images/loginpic.png"
        pixmap = QPixmap(image_path)

        label = QLabel(self.ui.rightcontainer)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 947, 827)
        label.setScaledContents(True)
    
    def open_signup_window(self):
        self.close()
        from app.template.signup.Signuprun import SignupWindow
        self.signup = SignupWindow()
        self.signup.show()

    def go_to_homepage(self):
        from app.template.homepage.Homepagerun import HomepageWindow
        self.home = HomepageWindow()
        self.close()
        self.home.show()

        
    def open_homepage(self):
        self.close()
        from app.template.homepage.Homepagerun import HomepageWindow
        self.login_window = HomepageWindow()
        self.login_window.show()
        
    def login_window(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        admin = False
        if self.ui.checkbox.isChecked():
            admin = True
        if login(username, password, admin):
            print("Login Successful")
            self.show_success("Login successful, welcome")
            self.open_homepage()
            
        else:
            print("Login Failed")
            self.ui.username.clear()
            self.ui.password.clear()
            # self.open_signup_window()
            self.show_error("Login failed, please try again")

    def show_success(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Login Succesful")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Login Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.login_window()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())