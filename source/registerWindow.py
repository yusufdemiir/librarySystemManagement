from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mysql.connector import Error
from database import Database as db

class register_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection = None
        self.cursor = None

        self.setObjectName("registerWindow")
        self.setFixedSize(600, 400)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Kayıt Ekranı')
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.IdLabel = QtWidgets.QLabel(self.centralwidget)
        self.IdLabel.setGeometry(QtCore.QRect(100, 43, 20, 16))
        self.IdLabel.setObjectName("nameLabel")
        self.IdLabel.setText('ID: ')
        self.IdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IdEdit.setGeometry(QtCore.QRect(213, 43, 241, 22))
        self.IdEdit.setObjectName("nameEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(250, 320, 100, 28))
        self.addButton.setObjectName("addButton")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(100, 73, 20, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setGeometry(QtCore.QRect(100, 102, 40, 16))
        self.surnameLabel.setObjectName("surnameLabel")
        self.tcNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.tcNoLabel.setGeometry(QtCore.QRect(100, 131, 77, 16))
        self.tcNoLabel.setObjectName("tcNoLabel")
        self.phoneNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneNoLabel.setGeometry(QtCore.QRect(100, 159, 106, 16))
        self.phoneNoLabel.setObjectName("phoneNoLabel")
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        self.addressLabel.setGeometry(QtCore.QRect(100, 215, 38, 16))
        self.addressLabel.setObjectName("addressLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 188, 38, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.surnameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameEdit.setGeometry(QtCore.QRect(213, 102, 241, 22))
        self.surnameEdit.setObjectName("surnameEdit")
        self.tcNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tcNoEdit.setGeometry(QtCore.QRect(213, 131, 241, 22))
        self.tcNoEdit.setObjectName("tcNoEdit")
        self.phoneNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneNoEdit.setGeometry(QtCore.QRect(213, 159, 241, 22))
        self.phoneNoEdit.setObjectName("phoneNoEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(213, 73, 241, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(213, 215, 241, 87))
        self.addressEdit.setObjectName("addressEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setGeometry(QtCore.QRect(213, 188, 241, 22))
        self.passwordEdit.setObjectName("passwordEdit")
        self.showPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPasswordButton.setGeometry(QtCore.QRect(455, 188, 28, 28))
        self.showPasswordButton.setObjectName("showPasswordButton")
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        self.showPasswordButton.setText("👁️")
        self.showPasswordButton.setFont(font2)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.addButton.clicked.connect(self.addButtonClick)
        self.showPasswordButton.clicked.connect(self.togglePasswordVisibility)
    
    def addButtonClick(self):
        print('Kayıt Olma butonuna tıklandı.')
        
        # Başarılır Kayıt Durumu:
        try:
            id_ = self.IdEdit.text()
            name = self.nameEdit.text()
            surname = self.surnameEdit.text()
            password = self.passwordEdit.text()
            tc = self.tcNoEdit.text()
            address = self.addressEdit.toPlainText()
            tel = self.phoneNoEdit.text()
            db_connect = db("localhost", "root", "123456", "zby_lms_db")
            self.db_connection = db_connect.create_connection()
            self.cursor = self.db_connection.cursor()
            sql = ("INSERT INTO users (user_id, name_, surname, password_, tel, address, tc) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            self.cursor.execute(sql, (id_, name, surname, password, tel, address, tc,))
            self.db_connection.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Kayıt Gerçekleşti")
            msg.setText("Kaydınız başarı ile gerçekleşti. Lütfen kullanıcı girişi yapınız.")
            msg.setIcon(QMessageBox.Information)
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap('../icons/checkMark.jpg'))
            msg.setWindowIcon(self.icon)
            msg.exec_()
            self.cursor.close()
            self.db_connection.close()
            self.close()
        # Başarısız Kayıt:
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Başarısız Kayıt!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Kayıt Olamama Sebebi: {}".format(str(e)))
            msg.exec_()

    # Şifre göster butonu fonksiyonu
    def togglePasswordVisibility(self):
        if self.passwordEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("userAddWindow", "Kayıt Ekranı"))
        self.addButton.setText(_translate("userAddWindow", "Kayıt Ol"))
        self.nameLabel.setText(_translate("userAddWindow", "Ad:"))
        self.surnameLabel.setText(_translate("userAddWindow", "Soyad:"))
        self.tcNoLabel.setText(_translate("userAddWindow", "TC Kimlik No:"))
        self.phoneNoLabel.setText(_translate("userAddWindow", "Telefon Numarası:"))
        self.addressLabel.setText(_translate("userAddWindow", "Adres:"))
        self.passwordLabel.setText(_translate('userAddWindow', 'Şifre:'))