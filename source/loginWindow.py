from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from userMainWindow import user_Main_Window
from adminMainWindow import admin_Main_Window
from registerWindow import register_Window
from database import Database as db
from mysql.connector import Error

class login_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection = None

        self.setObjectName("Giris Ekrani")
        self.setFixedSize(1200, 800)
        self.setWindowIcon(QIcon('../icons/logo.jpeg'))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(470, 490, 221, 61))
        self.enterButton.setObjectName("enterButton")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enterButton.setFont(font)

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(480, 555, 200, 50))
        self.registerButton.setText('Kayıt Ol')
        font = QtGui.QFont()
        font.setPointSize(8)
        self.registerButton.setFont(font)

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

        # Butonların fonksiyonlar ile bağlanması
        self.enterButton.clicked.connect(self.enterButtonClickHandler)
        self.userRadioButton.clicked.connect(self.userButtonHandler)
        self.adminRadioButton.clicked.connect(self.adminButtonHandler)
        self.showPasswordButton.clicked.connect(self.togglePasswordVisibility)
        self.registerButton.clicked.connect(self.registerButtonClick)

    # Giriş butonu fonksiyonu
    def enterButtonClickHandler(self):
        print("Giriş Butonuna Tıklandı.")
        entered_id = self.idLine.text()
        entered_password = self.passwordLine.text()
        db_connect = db("localhost", "root", "123456", "zby_lms_db")
        self.db_connection = db_connect.create_connection()
        entered_id_role = None
        verified_password = None
        if self.db_connection:
            verified_password = self.verify_user(entered_id)
            entered_id_role = self.fetchRole(entered_id)

        if (verified_password == entered_password
            and entered_id_role == "Ziyaretçi" and self.adminRadioButton.isChecked()):
            print("Kullanıcı yöneticiyi seçti")
            self.wrong_login(4)
        elif (verified_password == entered_password
              and entered_id_role == "Yönetici" and self.userRadioButton.isChecked()):
            print("Yönetici kullanıcıyı seçti")
            self.wrong_login(5)
        elif verified_password == entered_password:
            self.successful_login(entered_id)
        elif verified_password is None:
            if self.db_connection:
                print("Yanlış ID")
                self.wrong_login(1)
            else:
                print('Database hatası')
                self.wrong_login(3)
        elif verified_password != entered_password:
            print('Yanlış Şifre')
            self.wrong_login(2)
        elif entered_id_role is None:
            print("Rol kaydı yok")
            self.wrong_login(6)

    # Şifre göster butonu fonksiyonu
    def togglePasswordVisibility(self):
        if self.passwordLine.echoMode() == QtWidgets.QLineEdit.Password:
            self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)

    # Kullanıcı butonu fonksiyonu
    def userButtonHandler(self):
        self.idLabel.setText("Kullanıcı ID:")

    # Yönetici butonu fonksiyonu
    def adminButtonHandler(self):
        self.idLabel.setText("Yönetici ID:")

    # Başarılı giriş fonksiyonu
    def successful_login(self, entered_id):
        if self.adminRadioButton.isChecked():
            print('Yönetici Girişi Başarılır. Yönetici Paneline Geçildi.')
            self.startWindow = admin_Main_Window(self.db_connection, entered_id)
            self.startWindow.show()
            self.close()
        else:
            print('Kullanıcı girişi başarılı, Kullanıcı ekranına geçildi!!')
            self.startWindow = user_Main_Window(self.db_connection, entered_id)
            self.startWindow.show()
            self.close()

    # Kayıt olma butonu fonksiyonu
    def registerButtonClick(self):
        print('Kayıt Olma Butonuna Tıklandı.')
        self.startWindow = register_Window()
        self.startWindow.show()

    # Başarısız giriş fonksiyonu
    def wrong_login(self, err_num):
        msg = QMessageBox()
        msg.setWindowTitle("Giriş Başarısız!")
        if err_num == 1:
            msg.setText("ID nizi yanlış girdiniz. Lütfen tekrar deneyiniz.")
        elif err_num == 2:
            msg.setText("Şifrenizi yanliş girdiniz. Lütfen tekrar deneyiniz.")
        elif err_num == 3:
            msg.setText("Veri tabanina ulaşilamiyor. Biraz sonra tekrar deneyiniz.")
        elif err_num == 4:
            msg.setText("Yönetici erişimine sahip değilsiniz.")
        elif err_num == 5:
            msg.setText("Yönetici ID ile kullanıcı girişi denemesi. "
                        "Yönetici girişini seçin veya varsa kullanıcı ID nizle giriş yapın.")
        elif err_num == 6:
            msg.setText("Rolünüz belirlenmemiş.")
        msg.setIcon(QMessageBox.Critical)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('../icons/redXicon.png'))
        msg.setWindowIcon(icon)
        msg.exec_()

    # İsimlendirme fonksiyonu
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi - Giriş Sayfası"))
        self.enterButton.setText(_translate("MainWindow", "Giriş"))
        self.userRadioButton.setText(_translate("MainWindow", "Kullanıcı"))
        self.adminRadioButton.setText(_translate("MainWindow", "Yönetici"))
        self.idLabel.setText(_translate("MainWindow", "Kullanıcı ID:"))
        self.passwordLabel.setText(_translate("MainWindow", "Şifre:"))

    # Kullanıcı doğrulama fonksiyonu
    def verify_user(self, id_):
        cursor = self.db_connection.cursor()
        try:
            sql = "SELECT password_ FROM users WHERE user_id = %s"
            cursor.execute(sql, (id_,))
            password = cursor.fetchone()
            if password:
                return password[0]  # Şifreyi döndür
            else:
                return None  # Kullanıcı bulunamadıysa None döndür
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Doğrulama Yapılamadı!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()
        finally:
            if cursor:
                cursor.close()

    def fetchRole(self, entered_id):
        cursor = self.db_connection.cursor()
        try:
            sql = "SELECT role_ FROM users WHERE user_id = %s"
            cursor.execute(sql, (entered_id,))
            role = cursor.fetchone()
            if role:
                return role[0]
            else:
                return None
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kullanıcı Rolü Belirlenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()
