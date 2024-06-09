from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mysql.connector import Error

class show_Info(QMainWindow):
    def __init__(self, db_connection, cursor, selected_detail):
        super().__init__()
        self.db_connection = db_connection
        self.cursor = cursor

        self.setObjectName("showInfo")
        self.setFixedSize(600, 400)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

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

        self.summaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.summaryLabel.setGeometry(QtCore.QRect(97, 236, 38, 16))
        self.summaryLabel.setObjectName("summaryLabel")
        self.publisherEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.publisherEdit.setGeometry(QtCore.QRect(210, 120, 241, 22))
        self.publisherEdit.setObjectName("publisherEdit")
        self.publisherEdit.setReadOnly(True)

        self.barkodNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.barkodNoLabel.setGeometry(QtCore.QRect(97, 178, 106, 16))
        self.barkodNoLabel.setObjectName("barkodNoLabel")

        self.barkodNoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.barkodNoEdit.setGeometry(QtCore.QRect(210, 178, 241, 22))
        self.barkodNoEdit.setObjectName("barkodNoEdit")
        self.barkodNoEdit.setReadOnly(True)

        self.authorEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authorEdit.setGeometry(QtCore.QRect(210, 62, 241, 22))
        self.authorEdit.setObjectName("authorEdit")
        self.authorEdit.setReadOnly(True)

        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit.setGeometry(QtCore.QRect(210, 91, 241, 22))
        self.genreEdit.setObjectName("genreEdit")
        self.genreEdit.setReadOnly(True)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(210, 33, 241, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setReadOnly(True)
        self.addressEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(210, 236, 241, 87))
        self.addressEdit.setObjectName("addressEdit")
        self.addressEdit.setReadOnly(True)
        self.setCentralWidget(self.centralwidget)

        self.length = len(selected_detail)
        if self.length == 9:
            self.nameEdit.setText(selected_detail[1])
            self.authorEdit.setText(selected_detail[2])
            self.genreEdit.setText(selected_detail[3])
            self.barkodNoEdit.setText(selected_detail[5])
            self.publisherEdit.setText(selected_detail[4])
            self.addressEdit.setText(selected_detail[8])
        elif self.length == 1:
            try:
                sql = "SELECT book_name, author, genre, isbn, publisher, summary FROM book_pool WHERE book_id = %s"
                self.cursor.execute(sql, (selected_detail,))
                book_detail = self.cursor.fetchone()
                self.nameEdit.setText(book_detail[0])
                self.authorEdit.setText(book_detail[1])
                self.genreEdit.setText(book_detail[2])
                self.barkodNoEdit.setText(book_detail[3])
                self.publisherEdit.setText(book_detail[4])
                self.addressEdit.setText(book_detail[5])
            except Error as e:
                msg = QMessageBox()
                msg.setWindowTitle("Kitap Bilgileri Gösterilemedi!")
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                msg.setText("Hata Açıklaması: {}".format(str(e)))
                msg.exec_()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, userAddWindow):
        _translate = QtCore.QCoreApplication.translate
        userAddWindow.setWindowTitle(_translate("userAddWindow", "Detaylar"))
        self.nameLabel.setText(_translate("userAddWindow", "Kitap ismi:"))
        self.authorLabel.setText(_translate("userAddWindow", "Yazar:"))
        self.genreLabel.setText(_translate("userAddWindow", "Tür:"))
        self.publisherLabel.setText(_translate("userAddWindow", "Yayın Evi:"))
        self.summaryLabel.setText(_translate("userAddWindow", "Özet:"))
        self.barkodNoLabel.setText(_translate("userAddWindow", "Barkod No:"))