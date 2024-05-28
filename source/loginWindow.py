from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from userMainWindow import user_Main_Window
from adminMainWindow import admin_Main_Window
class login_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Giriş Ekrani")
        self.resize(1200, 800)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(470, 490, 221, 61))
        self.enterButton.setObjectName("enterButton")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterButton.setFont(font)
        
        
        self.showPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPasswordButton.setGeometry(QtCore.QRect(750, 425, 28, 28))
        self.showPasswordButton.setObjectName("showPasswordButton")
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        self.showPasswordButton.setText("👁️")
        self.showPasswordButton.setFont(font2)
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(380, 160, 501, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.userRadioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userRadioButton.setFont(font)
        self.userRadioButton.setObjectName("userRadioButton")
        self.gridLayout.addWidget(self.userRadioButton, 0, 0, 1, 1)
        self.userRadioButton.setChecked(True)
        
        self.adminRadioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.adminRadioButton.setFont(font)
        self.adminRadioButton.setObjectName("adminRadioButton")
        self.gridLayout.addWidget(self.adminRadioButton, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(420, 270, 321, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.idLabel = QtWidgets.QLabel(self.widget1)
        
        font = QtGui.QFont()
        font.setPointSize(15)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.verticalLayout.addWidget(self.idLabel)
        
        self.idLine = QtWidgets.QLineEdit(self.widget1)
        self.idLine.setObjectName("idLine")
        
        self.verticalLayout.addWidget(self.idLine)
        self.passwordLabel = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout.addWidget(self.passwordLabel)
        
        self.passwordLine = QtWidgets.QLineEdit(self.widget1)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        
        self.verticalLayout.addWidget(self.passwordLine)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.enterButton.clicked.connect(self.enterButtonClickHandler)
        self.userRadioButton.clicked.connect(self.userButtonHandler)
        self.adminRadioButton.clicked.connect(self.adminButtonHandler)
        
        def togglePasswordVisibility(self):
  
         if self.passwordLine.echoMode() == QtWidgets.QLineEdit.Password:
           self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Normal)
         else:
           self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
           
    def enterButtonClickHandler(self):
        print('Giriş Butonuna Tıklandı.')
        entered_id = self.idLine.text()
        entered_password = self.passwordLine.text()
        if entered_id.strip() == "admin" and entered_password.strip() == "password":
            self.successful_login()
        else:
            print('Başarısız Giriş.')
            self.wrong_login()
    
    def userButtonHandler(self):
        self.idLabel.setText("Kullanıcı ID:")

    def adminButtonHandler(self):
        self.idLabel.setText("Yönetici ID:")
        
    def successful_login(self):
        if self.adminRadioButton.isChecked():
            print('Yönetici Girişi Başarılır. Yönetici Paneline Geçildi.')
            self.startWindow = admin_Main_Window()
            self.startWindow.show()
            self.close()
        else:
            print('Kullanıcı Girişi Başarılı. Kullanıcı Ekranına Geçildi.')
            self.startWindow = user_Main_Window()
            self.startWindow.show()
            self.close()
        
        
    def wrong_login(self):
        msg = QMessageBox()
        msg.setWindowTitle("Giriş Başarısız!")
        msg.setText("ID veya şifrenizi yanlış girdiniz. Lütfen tekrar deneyiniz.")
        msg.setIcon(QMessageBox.Critical)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('icons/redXicon.png'))
        msg.setWindowIcon(self.icon)
        x = msg.exec_()
    
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi - Giriş Sayfası"))
        self.enterButton.setText(_translate("MainWindow", "Giriş"))
        self.userRadioButton.setText(_translate("MainWindow", "Kullanıcı"))
        self.adminRadioButton.setText(_translate("MainWindow", "Yönetici"))
        self.idLabel.setText(_translate("MainWindow", "Kullanıcı ID:"))
        self.passwordLabel.setText(_translate("MainWindow", "Şifre:"))
