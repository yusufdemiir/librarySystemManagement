from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mainWindow import main_Window
from database import Database as db
class login_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection = None

        self.setObjectName("Giriş Ekrani")
        self.resize(1200, 800)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(470, 490, 221, 61))
        self.enterButton.setObjectName("enterButton")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 700, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
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

        self.enterButton.clicked.connect(self.clickHandler)
        self.userRadioButton.clicked.connect(self.userButtonHandler)
        self.adminRadioButton.clicked.connect(self.adminButtonHandler)

    def clickHandler(self):
        print('Clicked!')
        entered_id = self.idLine.text()
        entered_password = self.passwordLine.text()
        db_connect = db("localhost", "root", "123456", "zby_lms_db")
        self.db_connection = db_connect.create_connection()
        if entered_id.strip() == "admin" and entered_password.strip() == "password" and self.db_connection:
            print('Giriş Başarili!!')
            self.successful_login()
        elif entered_id.strip() != "admin" and self.db_connection:
            print('Yanliş ID')
            self.wrong_login(1)
        elif (entered_id.strip() == "admin" and entered_password.strip() != "password"
              and self.db_connection):
            print('Yanliş Şifre')
            self.wrong_login(2)
        elif not self.db_connection:
            print('Database hatasi')
            self.wrong_login(3)
    
    def userButtonHandler(self):
        self.idLabel.setText("Ziyaretçi ID:")

    def adminButtonHandler(self):
        self.idLabel.setText("Yönetici ID:")
        
    def successful_login(self):
        print('Giriş başarili, Ana ekrana geçildi!!')
        self.startMainWindow = main_Window(self.db_connection)
        self.startMainWindow.show()
        self.close()

    def wrong_login(self, err_num):
        msg = QMessageBox()
        msg.setWindowTitle("Giriş Başarisiz!")
        if err_num == 1:
            msg.setText("ID kismini yanliş girdiniz. Lütfen yeniden deneyiniz.")
        elif err_num == 2:
            msg.setText("Şifre kismini yanliş girdiniz. Lütfen yeniden deneyiniz.")
        elif err_num == 3:
            msg.setText("Veri tabanina ulaşilamiyor. Biraz sonra tekrar deneyiniz.")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enterButton.setText(_translate("MainWindow", "Giriş"))
        self.label.setText(_translate("MainWindow", "Yeni kullanici iseniz lütfen bir yönetici ile iletişime geçin."))
        self.userRadioButton.setText(_translate("MainWindow", "Ziyaretçi"))
        self.adminRadioButton.setText(_translate("MainWindow", "Yönetici"))
        self.idLabel.setText(_translate("MainWindow", "Ziyaretçi ID:"))
        self.passwordLabel.setText(_translate("MainWindow", "Şifre:"))
