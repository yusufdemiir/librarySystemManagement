from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from mysql.connector import Error
import random, string

class add_User_Window(QMainWindow):
    def __init__(self, db_connection, cursor):
        super().__init__()
        self.db_connection = db_connection
        self.cursor = cursor
        
        self.setObjectName("userAddWindow")
        self.setFixedSize(600, 400)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(250, 350, 100, 28))
        self.addButton.setObjectName("addButton")
        self.userRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.userRadioButton.setGeometry(QtCore.QRect(229, 39, 73, 20))
        self.userRadioButton.setObjectName("userRadioButton")
        self.adminRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.adminRadioButton.setGeometry(QtCore.QRect(345, 39, 71, 20))
        self.adminRadioButton.setObjectName("adminRadioButton")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(100, 40, 82, 16))
        self.userLabel.setObjectName("userLabel")
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
        self.phoneNoLabel.setGeometry(QtCore.QRect(100, 189, 106, 16))
        self.phoneNoLabel.setObjectName("phoneNoLabel")
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        self.addressLabel.setGeometry(QtCore.QRect(100, 247, 38, 16))
        self.addressLabel.setObjectName("addressLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 218, 38, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.surnameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameEdit.setGeometry(QtCore.QRect(213, 102, 241, 22))
        self.surnameEdit.setObjectName("surnameEdit")
        self.tcNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tcNoEdit.setGeometry(QtCore.QRect(213, 131, 241, 22))
        self.tcNoEdit.setObjectName("tcNoEdit")
        self.phoneNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneNoEdit.setGeometry(QtCore.QRect(213, 189, 241, 22))
        self.phoneNoEdit.setObjectName("phoneNoEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(213, 73, 241, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(213, 247, 241, 87))
        self.addressEdit.setObjectName("addressEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setGeometry(QtCore.QRect(213, 218, 241, 22))
        self.passwordEdit.setObjectName("passwordEdit")
        self.showPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.showPasswordButton.setGeometry(QtCore.QRect(455, 218, 28, 28))
        self.showPasswordButton.setObjectName("showPasswordButton")
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        self.showPasswordButton.setText("👁️")
        self.showPasswordButton.setFont(font2)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.addButton.clicked.connect(self.addClick)
        self.showPasswordButton.clicked.connect(self.togglePasswordVisibility)
        
    # Ekleme butonu fonksiyonu
    def addClick(self):
        name = self.nameEdit.text()
        surname = self.surnameEdit.text()
        password = self.passwordEdit.text()
        tel = self.phoneNoEdit.text()
        address = self.addressEdit.toPlainText()
        tc = self.tcNoEdit.text()
        id_chars = string.ascii_letters + string.digits
        id_ = "".join(random.choice(id_chars) for _ in range(15))
        try:
            sql = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            if self.adminRadioButton.isChecked():
                self.cursor.execute(sql, (id_, name, surname, password, "Yönetici", tel, address, tc,))
                self.db_connection.commit()
            elif self.userRadioButton.isChecked():
                self.cursor.execute(sql, (id_, name, surname, password, "Ziyaretçi", tel, address, tc,))
                self.db_connection.commit()
            print("Kullanıcı Eklendi")
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kullanıcı Eklenemedi")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Şifre göster butonu fonksiyonu
    def togglePasswordVisibility(self):
        if self.passwordEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    # İsimlendirme
    def retranslateUi(self, userAddWindow):
        _translate = QtCore.QCoreApplication.translate
        userAddWindow.setWindowTitle(_translate("userAddWindow", "Kullanıcı Ekleme Paneli"))
        self.addButton.setText(_translate("userAddWindow", "Ekle"))
        self.userRadioButton.setText(_translate("userAddWindow", "Kullanıcı"))
        self.adminRadioButton.setText(_translate("userAddWindow", "Yönetici"))
        self.userLabel.setText(_translate("userAddWindow", "Kullanıcı Türü:"))
        self.nameLabel.setText(_translate("userAddWindow", "Ad:"))
        self.surnameLabel.setText(_translate("userAddWindow", "Soyad:"))
        self.tcNoLabel.setText(_translate("userAddWindow", "TC Kimlik No:"))
        self.phoneNoLabel.setText(_translate("userAddWindow", "Telefon Numarası:"))
        self.addressLabel.setText(_translate("userAddWindow", "Adres:"))
        self.passwordLabel.setText(_translate('userAddWindow', 'Şifre:'))
        