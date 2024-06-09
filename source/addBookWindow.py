from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mysql.connector import Error

class add_Book_Window(QMainWindow):
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
        self.addButton.setGeometry(QtCore.QRect(250, 340, 100, 28))
        self.addButton.setObjectName("addButton")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(97, 33, 71, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(97, 62, 40, 16))
        self.authorLabel.setObjectName("authorLabel")
        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel.setGeometry(QtCore.QRect(97, 91, 77, 16))
        self.genreLabel.setObjectName("genreLabel")
        self.publisherLabel = QtWidgets.QLabel(self.centralwidget)
        self.publisherLabel.setGeometry(QtCore.QRect(97, 120, 82, 16))
        self.publisherLabel.setObjectName("publisherLabel")
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(97, 149, 106, 16))
        self.numberLabel.setObjectName("numberLabel")
        self.summaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.summaryLabel.setGeometry(QtCore.QRect(97, 236, 38, 16))
        self.summaryLabel.setObjectName("summaryLabel")
        self.publisherEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.publisherEdit.setGeometry(QtCore.QRect(210, 120, 241, 22))
        self.publisherEdit.setObjectName("publisherEdit")
        self.numberEdit = QtWidgets.QSpinBox(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(210, 150, 241, 22))
        self.numberEdit.setObjectName("numberEdit")
        self.barkodNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.barkodNoLabel.setGeometry(QtCore.QRect(97, 178, 106, 16))
        self.barkodNoLabel.setObjectName("barkodNoLabel")

        self.barkodNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.barkodNoEdit.setGeometry(QtCore.QRect(210, 178, 241, 22))
        self.barkodNoEdit.setObjectName("barkodNoEdit")

        self.authorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorEdit.setGeometry(QtCore.QRect(210, 62, 241, 22))
        self.authorEdit.setObjectName("authorEdit")
        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit.setGeometry(QtCore.QRect(210, 91, 241, 22))
        self.genreEdit.setObjectName("genreEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(210, 33, 241, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(210, 236, 241, 87))
        self.addressEdit.setObjectName("addressEdit")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.addButton.clicked.connect(self.addClick)

    # Ekleme butonu fonksiyonu
    def addClick(self):
        print('Ekleme Butonuna Tıklandı.')
        name = self.nameEdit.text()
        author = self.authorEdit.text()
        genre = self.genreEdit.text()
        publisher = self.publisherEdit.text()
        isbn = self.barkodNoEdit.text()
        summary = self.addressEdit.toPlainText()
        try:
            sql = ("INSERT INTO book_pool (book_name, author, genre, publisher, isbn, summary) "
                   "VALUES(%s, %s, %s, %s, %s, %s)")
            self.cursor.execute(sql, (name, author, genre, publisher, isbn, summary,))
            self.db_connection.commit()
            print("Kitap Eklendi!")
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Eklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # İsimlendirme
    def retranslateUi(self, userAddWindow):
        _translate = QtCore.QCoreApplication.translate
        userAddWindow.setWindowTitle(_translate("userAddWindow", "Kitap Ekleme Paneli"))
        self.addButton.setText(_translate("userAddWindow", "Ekle"))
        self.nameLabel.setText(_translate("userAddWindow", "Kitap ismi:"))
        self.authorLabel.setText(_translate("userAddWindow", "Yazar:"))
        self.genreLabel.setText(_translate("userAddWindow", "Tür:"))
        self.publisherLabel.setText(_translate("userAddWindow", "Yayın Evi:"))
        self.numberLabel.setText(_translate("userAddWindow", "Adet:"))
        self.summaryLabel.setText(_translate("userAddWindow", "Özet:"))
        self.barkodNoLabel.setText(_translate("userAddWindow", "Barkod No:"))