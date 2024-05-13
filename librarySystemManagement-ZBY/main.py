from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from login import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.enterButton.clicked.connect(self.clickHandler)
        self.userRadioButton.clicked.connect(self.userButtonHandler)
        self.adminRadioButton.clicked.connect(self.adminButtonHandler)
    
    def clickHandler(self):
        print('Clicked!')
        entered_id = self.idLine.text()
        entered_password = self.passwordLine.text()
        if entered_id.strip() == "admin" and entered_password.strip() == "password":
            print('Giriş Başarılı!!')
            self.successful_login()
        else:
            print('Yanlış ID veya Şifre')
            self.wrong_login()
    
    def userButtonHandler(self):
        self.idLabel.setText("Ziyaretçi ID:")
    def adminButtonHandler(self):
        self.idLabel.setText("Yönetici ID:")
        
    def successful_login(self):
        msg = QMessageBox()
        msg.setWindowTitle("Giriş Başarılı!")
        msg.setText("Başarılı bir giriş gerçekleştirdiniz.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    def wrong_login(self):
        msg = QMessageBox()
        msg.setWindowTitle("Giriş Başarısız!")
        msg.setText("ID veya Şifre kısmını yanlış girdiniz. Lütfen yeniden deneyiniz.")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
        
app = QApplication([])
window = Window()

window.show()
app.exec()