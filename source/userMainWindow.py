from collections import deque
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QMessageBox, QTableWidgetItem
from showInfo import show_Info
from mysql.connector import Error

class user_Main_Window(QMainWindow):
    def __init__(self, db_connection, entered_id):
        super().__init__()
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()
        self.q = deque()
        self.q_index = []

        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Giriş Frame
        self.welcomeFrame = QtWidgets.QFrame(self.centralwidget)
        self.welcomeFrame.setGeometry(QtCore.QRect(170, 10, 621, 531))
        self.welcomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcomeFrame.setObjectName("welcomeFrame")
        self.iconLabel = QtWidgets.QLabel(self.welcomeFrame)
        self.iconLabel.setGeometry(QtCore.QRect(120, 40, 391, 381))
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("../icons/logo.jpeg"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.welcomeFrame)
        self.welcomeLabel.setGeometry(QtCore.QRect(210, 440, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")

        # Kitaplar Frame
        self.booksFrame = QtWidgets.QFrame(self.centralwidget)
        self.booksFrame.setEnabled(True)
        self.booksFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.booksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksFrame.setObjectName("booksFrame")
        self.booksLabel = QtWidgets.QLabel(self.booksFrame)
        self.booksLabel.setGeometry(QtCore.QRect(20, 0, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.booksLabel.setFont(font)
        self.booksLabel.setObjectName("welcomeLabel")
        self.booksTable = QtWidgets.QTableWidget(self.booksFrame)
        self.booksTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.booksTable.setObjectName("booksTable")
        self.booksTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.takeBookButton = QtWidgets.QPushButton(self.booksFrame)
        self.takeBookButton.setGeometry(QtCore.QRect(470, 470, 111, 31))
        self.takeBookButton.setObjectName("takeBookButton")
        self.reservationButton = QtWidgets.QPushButton(self.booksFrame)
        self.reservationButton.setGeometry(QtCore.QRect(359, 470, 111, 31))
        self.reservationButton.setObjectName('reservationButton')
        self.widget = QtWidgets.QWidget(self.booksFrame)
        self.widget.setGeometry(QtCore.QRect(230, 10, 351, 87))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel = QtWidgets.QLabel(self.widget)
        self.searchLabel.setObjectName("searchLabel")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchLabel.setFont(font)
        self.horizontalLayout.addWidget(self.searchLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setText("")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/search-icon.jpg'))
        self.searchButton.setIcon(self.icon)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.showAll = QtWidgets.QPushButton(self.booksFrame)
        self.showAll.setText('Hepsini Göster')
        self.showAll.setGeometry(QtCore.QRect(2, 470, 90, 31, ))
        self.showDetails = QtWidgets.QPushButton(self.booksFrame)
        self.showDetails.setText('Ayrıntıları Göster')
        self.showDetails.setGeometry(QtCore.QRect(93, 470, 110, 31, ))
        self.booksFrame.hide()

        # Kitaplarım Frame

        self.myBooksFrame = QtWidgets.QFrame(self.centralwidget)
        self.myBooksFrame.setEnabled(True)
        self.myBooksFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.myBooksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.myBooksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.myBooksFrame.setObjectName("myBooksFrame")
        self.myBooksLabel = QtWidgets.QLabel(self.myBooksFrame)
        self.myBooksLabel.setGeometry(QtCore.QRect(20, 0, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.myBooksLabel.setFont(font)
        self.myBooksLabel.setObjectName("myBooksLabel")
        self.myBooksTable = QtWidgets.QTableWidget(self.myBooksFrame)
        self.myBooksTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.myBooksTable.setObjectName("myBooksTable")
        self.myBooksTable.setEditTriggers(QTableWidget.NoEditTriggers)

        self.leaveBookButton = QtWidgets.QPushButton(self.myBooksFrame)
        self.leaveBookButton.setGeometry(QtCore.QRect(470, 470, 111, 31))
        self.leaveBookButton.setObjectName("leaveBookButton")
        self.widget = QtWidgets.QWidget(self.myBooksFrame)
        self.widget.setGeometry(QtCore.QRect(230, 10, 351, 87))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel2 = QtWidgets.QLabel(self.widget)
        self.searchLabel2.setObjectName("searchLabel2")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchLabel2.setFont(font)
        self.horizontalLayout.addWidget(self.searchLabel2)
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.myBooksSearchButton = QtWidgets.QPushButton(self.widget)
        self.myBooksSearchButton.setText("")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/search-icon.jpg'))
        self.myBooksSearchButton.setIcon(self.icon)
        self.myBooksSearchButton.setObjectName("myBooksButton")
        self.horizontalLayout.addWidget(self.myBooksSearchButton)
        self.showAll2 = QtWidgets.QPushButton(self.myBooksFrame)
        self.showAll2.setText('Hepsini Göster')
        self.showAll2.setGeometry(QtCore.QRect(2, 470, 90, 31, ))
        self.showDetails2 = QtWidgets.QPushButton(self.myBooksFrame)
        self.showDetails2.setText('Ayrıntıları Göster')
        self.showDetails2.setGeometry(QtCore.QRect(93, 470, 110, 31, ))
        self.myBooksFrame.hide()

        # Rezervasyonlarım Frame
        self.myReservationsFrame = QtWidgets.QFrame(self.centralwidget)
        self.myReservationsFrame.setEnabled(True)
        self.myReservationsFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.myReservationsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.myReservationsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.myReservationsFrame.setObjectName("myBooksFrame")
        self.myReservationsLabel = QtWidgets.QLabel(self.myReservationsFrame)
        self.booksLabel.setGeometry(QtCore.QRect(20, 0, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.myReservationsLabel.setFont(font)
        self.myReservationsLabel.setObjectName("welcomeLabel")
        self.myReservationsLabel.setText('Rezervasyonlarım')
        self.myReservationsTable = QtWidgets.QTableWidget(self.myReservationsFrame)
        self.myReservationsTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.myReservationsTable.setObjectName("myBooksTable")

        self.myReservationsTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cancelReservationButton = QtWidgets.QPushButton(self.myReservationsFrame)
        self.cancelReservationButton.setGeometry(QtCore.QRect(435, 470, 145, 31))
        self.cancelReservationButton.setObjectName("cancelReservationButton")
        self.cancelReservationButton.setText('Rezervasyonu İptal Et')
        self.myReservationsFrame.hide()

        # Profil Frame
        try:
            sql = "SELECT user_id, name_, surname, tel, address, tc, password_ FROM users WHERE user_id = %s"
            self.cursor.execute(sql, (entered_id,))
            self.profile_details = self.cursor.fetchone()
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Profil Bilgileri Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

        self.profileFrame = QtWidgets.QFrame(self.centralwidget)
        self.profileFrame.setEnabled(True)
        self.profileFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.profileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileFrame.setObjectName("profileFrame")
        self.checkLabel = QtWidgets.QLabel(self.profileFrame)
        self.checkLabel.setGeometry(QtCore.QRect(396, 430, 28, 28))
        self.checkLabel.setObjectName('checkLabel')
        self.checkLabel.setText('')
        self.checkLabel.setPixmap(QtGui.QPixmap("../icons/checkMark.jpg"))
        self.checkLabel.setScaledContents(True)
        self.checkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.checkLabel.hide()
        self.profileLabel = QtWidgets.QLabel(self.profileFrame)
        self.profileLabel.setGeometry(QtCore.QRect(20, 0, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.profileLabel.setFont(font)
        self.profileLabel.setObjectName("profileLabel")
        self.profileEditButton = QtWidgets.QPushButton(self.profileFrame)
        self.profileEditButton.setGeometry(QtCore.QRect(210, 430, 93, 28))
        self.profileEditButton.setObjectName("profileEditButton")
        self.profileSaveButton = QtWidgets.QPushButton(self.profileFrame)
        self.profileSaveButton.setGeometry(QtCore.QRect(303, 430, 93, 28))
        self.profileSaveButton.setObjectName('profileSaveButton')
        self.widget = QtWidgets.QWidget(self.profileFrame)
        self.widget.setGeometry(QtCore.QRect(60, 100, 391, 301))
        self.widget.setObjectName("widget")
        self.profileLayout = QtWidgets.QGridLayout(self.widget)
        self.profileLayout.setContentsMargins(0, 0, 0, 0)
        self.profileLayout.setObjectName("profileLayout")
        self.addressLabel = QtWidgets.QLabel(self.widget)
        self.addressLabel.setObjectName("addressLabel")
        self.profileLayout.addWidget(self.addressLabel, 6, 0, 1, 1)
        self.surnameEditLine = QtWidgets.QLineEdit(self.widget)
        self.surnameEditLine.setObjectName("surnameEditLine")
        self.surnameEditLine.setReadOnly(True)
        self.profileLayout.addWidget(self.surnameEditLine, 2, 1, 1, 1)
        self.tcNoLabel = QtWidgets.QLabel(self.widget)
        self.tcNoLabel.setObjectName("tcNoLabel")
        self.profileLayout.addWidget(self.tcNoLabel, 3, 0, 1, 1)
        self.phoneNoLabel = QtWidgets.QLabel(self.widget)
        self.phoneNoLabel.setObjectName("phoneNoLabel")
        self.profileLayout.addWidget(self.phoneNoLabel, 5, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLineEdit.setReadOnly(True)
        self.profileLayout.addWidget(self.nameLineEdit, 1, 1, 1, 1)
        self.phoneNoEditLine = QtWidgets.QLineEdit(self.widget)
        self.phoneNoEditLine.setObjectName("phoneNoEditLine")
        self.phoneNoEditLine.setReadOnly(True)
        self.profileLayout.addWidget(self.phoneNoEditLine, 5, 1, 1, 1)
        self.tcNoEditLine = QtWidgets.QLineEdit(self.widget)
        self.tcNoEditLine.setObjectName("tcNoEditLine")
        self.tcNoEditLine.setReadOnly(True)
        self.profileLayout.addWidget(self.tcNoEditLine, 3, 1, 1, 1)
        self.addressEdit = QtWidgets.QTextEdit(self.widget)
        self.addressEdit.setObjectName("addressEdit")
        self.addressEdit.setReadOnly(True)
        self.profileLayout.addWidget(self.addressEdit, 6, 1, 1, 1)
        self.surnameLabel = QtWidgets.QLabel(self.widget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.profileLayout.addWidget(self.surnameLabel, 2, 0, 1, 1)
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setObjectName("nameLabel")
        self.profileLayout.addWidget(self.nameLabel, 1, 0, 1, 1)
        self.idLabel = QtWidgets.QLabel(self.widget)
        self.idLabel.setObjectName("idLabel")
        self.profileLayout.addWidget(self.idLabel, 0, 0, 1, 1)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setObjectName("idLineEdit")
        self.idLineEdit.setReadOnly(True)
        self.profileLayout.addWidget(self.idLineEdit, 0, 1, 1, 1)
        self.birthLabel = QtWidgets.QLabel(self.widget)
        self.birthLabel.setObjectName("birthLabel")
        self.profileLayout.addWidget(self.birthLabel, 4, 0, 1, 1)
        self.birthEdit = QtWidgets.QLineEdit(self.widget)
        self.birthEdit.setObjectName("birthEdit")
        self.birthEdit.setReadOnly(True)
        self.birthEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.profileLayout.addWidget(self.birthEdit, 4, 1, 1, 1)
        self.showPasswordButton = QtWidgets.QPushButton(self.profileFrame)
        self.showPasswordButton.setObjectName("showPasswordButton")
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        self.showPasswordButton.setText("👁️")
        self.showPasswordButton.setFont(font2)
        self.showPasswordButton.setGeometry(460, 250, 28, 28)
        self.profileFrame.hide()

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 10, 21, 531))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 141, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.booksButton = QtWidgets.QPushButton(self.widget)
        self.booksButton.setObjectName("booksButton")
        self.verticalLayout.addWidget(self.booksButton)
        self.myBooksButton = QtWidgets.QPushButton(self.widget)
        self.myBooksButton.setObjectName("myBooksButton")
        self.verticalLayout.addWidget(self.myBooksButton)
        self.myReservations = QtWidgets.QPushButton(self.widget)
        self.myReservations.setObjectName('myReservations')
        self.verticalLayout.addWidget(self.myReservations)
        self.profileButton = QtWidgets.QPushButton(self.widget)
        self.profileButton.setObjectName("profileButton")
        self.verticalLayout.addWidget(self.profileButton)
        self.logoutButton = QtWidgets.QPushButton(self.widget)
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout.addWidget(self.logoutButton)
        self.exitButton = QtWidgets.QPushButton(self.widget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Butonların Fonksiyonlar ile Bağlanması
        self.booksButton.clicked.connect(self.booksClick)
        self.myBooksButton.clicked.connect(lambda: self.myBooksClick(entered_id))
        self.profileButton.clicked.connect(self.profileClick)
        self.logoutButton.clicked.connect(self.logoutClick)
        self.profileEditButton.clicked.connect(self.profileEditClick)
        self.profileSaveButton.clicked.connect(lambda: self.profileSaveClick(entered_id))
        self.reservationButton.clicked.connect(lambda: self.reservationClick(entered_id))
        self.searchButton.clicked.connect(self.booksSearchClick)
        self.myBooksSearchButton.clicked.connect(self.myBooksSearchClick)
        self.showAll.clicked.connect(self.showAllClick)
        self.showAll2.clicked.connect(self.showAllClick2)
        self.myReservations.clicked.connect(lambda: self.myReservationsClick(entered_id))
        self.cancelReservationButton.clicked.connect(lambda: self.cancelReservationClick(entered_id))
        self.takeBookButton.clicked.connect(lambda: self.takeBookClick(entered_id))
        self.leaveBookButton.clicked.connect(self.leaveBookClick)
        self.showDetails.clicked.connect(self.showDetailsClick)
        self.showDetails2.clicked.connect(self.showDetailsClick2)
        self.showPasswordButton.clicked.connect(self.togglePasswordVisibility)
        self.exitButton.clicked.connect(self.closeApplicationClick)

    # Kitaplar butonu fonskiyonu:
    def booksClick(self):
        print('Kitaplar Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.myBooksFrame.hide()
        self.profileFrame.hide()
        self.myReservationsFrame.hide()
        self.booksFrame.show()
        self.load_books()

    # Mevcut kitapları gösteren metot
    def load_books(self):
        try:
            sql = "SELECT * FROM book_pool"
            self.cursor.execute(sql)
            books = self.cursor.fetchall()
            self.booksTable.setRowCount(len(books))
            self.booksTable.setColumnCount(9)

            for row_index, row_data in enumerate(books):
                for col_index, cell_data in enumerate(row_data):
                    self.booksTable.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))
            table_header = ["ID", "Kitap Adı", "Yazar", "Tür", "Yayın", "Barkod No", "Var/Yok", "Eklenme Tarihi", "Özeti"]
            self.booksTable.setHorizontalHeaderLabels(table_header)
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kitaplar Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Kitaplarım butonu fonksiyonu:
    def myBooksClick(self, entered_id):
        print("Kitaplarım butonuna tıklandı.")
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.profileFrame.hide()
        self.myReservationsFrame.hide()
        self.myBooksFrame.show()
        self.load_my_books(entered_id)

    # Kullanıcıya ait kitapları gösteren metot
    def load_my_books(self, entered_id):
        try:
            sql = ("SELECT borrow_id, borrowed_book_id, borrowed_date FROM borrowed_books "
                   "WHERE borrowed_user_id = %s AND return_date IS NULL")
            self.cursor.execute(sql, (entered_id,))
            myBooks = self.cursor.fetchall()
            self.myBooksTable.setRowCount(len(myBooks))
            self.myBooksTable.setColumnCount(3)

            for row_index, row_data in enumerate(myBooks):
                for col_index, cell_data in enumerate(row_data):
                    self.myBooksTable.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))
            row_headers = [str(i + 1) for i in range(len(myBooks))]
            self.myBooksTable.setVerticalHeaderLabels(row_headers)
            table_header = ["Alım ID", "Kitap ID", "Alım Tarihi"]
            self.myBooksTable.setHorizontalHeaderLabels(table_header)
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kitaplarınız Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Rezervasyonlarım butonu fonksiyonu:
    def myReservationsClick(self, entered_id):
        print('Rezervasyonlarım Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.myBooksFrame.hide()
        self.profileFrame.hide()
        self.myReservationsFrame.show()
        try:
            sql = ("SELECT b.book_name FROM book_pool b "
                   "JOIN reservations r ON b.book_id = r.reserved_book_id WHERE r.reserved_user_id = %s")
            self.cursor.execute(sql, (entered_id,))
            book_names = self.cursor.fetchall()
            self.myReservationsTable.setRowCount(len(book_names))
            self.myReservationsTable.setColumnCount(2)

            for row_index, row_data in enumerate(book_names):
                cell_data = row_data[0]
                self.myReservationsTable.setItem(row_index, 0, QTableWidgetItem(str(cell_data)))

            sql = "SELECT queue_no FROM reservations WHERE reserved_user_id = %s"
            self.cursor.execute(sql, (entered_id,))
            queue_nums = self.cursor.fetchall()

            for row_index, row_data in enumerate(queue_nums):
                index2 = 0
                cell_data = queue_nums[row_index][index2]
                self.myReservationsTable.setItem(row_index, 1, QTableWidgetItem(str(cell_data)))
                index2 += 1

            table_header = ["Kitap Adı", "Sıranız"]
            self.myReservationsTable.setHorizontalHeaderLabels(table_header)
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Rezervasyonlarınız Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Profil butonu fonksiyonu:
    def profileClick(self):
        print('Profil Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.myBooksFrame.hide()
        self.myReservationsFrame.hide()
        self.profileFrame.show()
        self.surnameEditLine.setText(self.profile_details[2])
        self.nameLineEdit.setText(self.profile_details[1])
        self.tcNoEditLine.setText(self.profile_details[5])
        self.addressEdit.setText(self.profile_details[4])
        self.idLineEdit.setText(self.profile_details[0])
        self.phoneNoEditLine.setText(self.profile_details[3])
        self.birthEdit.setText(self.profile_details[6])

    # Çıkış yapma butonu fonksiyonu
    def logoutClick(self):
        print('Çıkış Butonuna Tıklandı.')
        from loginWindow import login_Window
        self.startLoginWindow = login_Window()
        self.startLoginWindow.show()
        self.close()
        if self.db_connection:
            self.cursor.close()
            self.db_connection.close()
            print("Veri tabanı bağlantısı kapatıldı.")
        print('Giriş Ekranına Geçildi.')

    # Profil düzenleme butonu fonksiyonu
    def profileEditClick(self):
        print('Profil Düzenleme Butonuna Tıklandı.')
        self.nameLineEdit.setReadOnly(False)
        self.surnameEditLine.setReadOnly(False)
        self.phoneNoEditLine.setReadOnly(False)
        self.addressEdit.setReadOnly(False)
        self.idLineEdit.setReadOnly(False)
        self.birthEdit.setReadOnly(False)
        self.checkLabel.hide()

    # Kaydetme butonu fonksiyonu
    def profileSaveClick(self, entered_id):
        print('Profili Kaydet Butonuna Tıklandı.')
        self.idLineEdit.setReadOnly(True)
        self.nameLineEdit.setReadOnly(True)
        self.surnameEditLine.setReadOnly(True)
        self.phoneNoEditLine.setReadOnly(True)
        self.addressEdit.setReadOnly(True)
        self.birthEdit.setReadOnly(True)
        id_ = self.idLineEdit.text()
        name = self.nameLineEdit.text()
        surname = self.surnameEditLine.text()
        phoneNo = self.phoneNoEditLine.text()
        address = self.addressEdit.toPlainText()
        password_ = self.birthEdit.text()
        try:
            if id_ != self.profile_details[0]:
                sql = "UPDATE users SET user_id = %s WHERE user_id = %s"
                self.cursor.execute(sql, (id_, self.profile_details[0],))
                self.db_connection.commit()
            if name != self.profile_details[1]:
                sql = "UPDATE users SET name_ = %s WHERE user_id = %s"
                self.cursor.execute(sql, (name, self.profile_details[0],))
                self.db_connection.commit()
            if surname != self.profile_details[2]:
                sql = "UPDATE users SET surname = %s WHERE user_id = %s"
                self.cursor.execute(sql, (surname, self.profile_details[0],))
                self.db_connection.commit()
            if phoneNo != self.profile_details[3]:
                sql = "UPDATE users SET tel = %s WHERE user_id = %s"
                self.cursor.execute(sql, (phoneNo, self.profile_details[0],))
                self.db_connection.commit()
            if address != self.profile_details[4]:
                sql = "UPDATE users SET address = %s WHERE user_id = %s"
                self.cursor.execute(sql, (address, self.profile_details[0],))
                self.db_connection.commit()
            if password_ != self.profile_details[6]:
                sql = "UPDATE users SET password_ = %s WHERE user_id = %s"
                self.cursor.execute(sql, (password_, self.profile_details[0],))
                self.db_connection.commit()
            print("Değişiklik işlendi.")
            self.checkLabel.show()
            sql = "SELECT user_id, name_, surname, tel, address, tc FROM users WHERE user_id = %s"
            self.cursor.execute(sql, (entered_id,))
            self.profile_details = self.cursor.fetchone()
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Değişiklik Yapılamadı!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Uygulamayı Kapat Tuşu
    def closeApplicationClick(self):
        # Veritabanı bağlantısını kapatma
        if self.db_connection:
            self.cursor.close()
            self.db_connection.close()
            print("Veri tabanı bağlantısı kapatıldı")
            # Uygulamayı kapatma
        QApplication.quit()

    # Kitap alma butonu fonksiyonu
    def takeBookClick(self, entered_id):
        print('Kitap Alma Butonuna Tıklandı.')
        current_item = self.booksTable.currentRow()
        if current_item != -1:
            book_id_index = self.booksTable.item(current_item, 0)
            book_id = book_id_index.text()
            book_isAvailable = self.booksTable.item(current_item, 6)
            book_isAvailable_text = book_isAvailable.text()

            msg = QMessageBox().question(self, "Kitap Alma", "Almak istediğinize emin misiniz?",
                                         QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.Yes:
                if book_isAvailable_text == "1":
                    try:
                        sql = "INSERT INTO borrowed_books (borrowed_book_id, borrowed_user_id) VALUES (%s, %s)"
                        self.cursor.execute(sql, (book_id, entered_id,))
                        self.db_connection.commit()
                        print("Kitap Alındı")
                    except Error as e:
                        msg = QMessageBox()
                        msg.setWindowTitle("Kitap Alınamadı!")
                        msg.setIcon(QMessageBox.Critical)
                        msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                        msg.setText("Hata Açıklaması: {}".format(str(e)))
                        msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Kitap Mevcut Değil!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                    msg.setText("Kitap başkası tarafından alınmış. İsterseniz rezervasyon yapabilirsiniz.")
                    msg.exec_()
            else:
                print("Hayır a basıldı")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Kitap seçimi yapınız.")
            msg.exec_()

    # Kitap bırakma butonu fonksiyonu
    def leaveBookClick(self):
        print('Kitap Bırakma Butonuna Tıklandı.')
        current_item = self.myBooksTable.currentRow()
        if current_item != -1:
            borrow_id_index = self.myBooksTable.item(current_item, 0)
            borrow_id = borrow_id_index.text()
            returned_book_id_index = self.myBooksTable.item(current_item, 1)
            returned_book_id = returned_book_id_index.text()
            msg = QMessageBox().question(self, "Kitap Bırakma", "Bırakmak istediğinize emin misiniz?",
                                         QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.Yes:
                try:
                    sql = "CALL add_return_date (%s, %s)"
                    self.cursor.execute(sql, (borrow_id, returned_book_id,))
                    self.db_connection.commit()
                    self.myBooksTable.removeRow(current_item)
                    print("Kitap Bırakıldı")
                except Error as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Kitap Bırakılamadı!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                    msg.setText("Hata Açıklaması: {}".format(str(e)))
                    msg.exec_()
            else:
                print("Hayır a basıldı")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Kitap seçimi yapınız.")
            msg.exec_()

    # Rezervasyon butonu fonksyionu
    def reservationClick(self, entered_id):
        print('Rezervasyon Butonuna Tıklandı.')
        current_book = self.booksTable.currentRow()
        id_column_index = 0
        is_available_column_index = 6
        book_id = self.booksTable.item(current_book, id_column_index)
        is_available = self.booksTable.item(current_book, is_available_column_index)

        if current_book != -1:
            book_id_text = book_id.text()
            is_available_text = is_available.text()
            if is_available_text == "1":
                msg = QMessageBox()
                msg.setWindowTitle("Rezerve Edilemez!")
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                msg.setText("Mevcut olan kitaplar için rezervasyon hizmetimiz bulunmamaktadır.")
                msg.exec_()
            else:
                try:
                    sql = ("SELECT COUNT(*) FROM reservations "
                           "INNER JOIN book_pool ON reservations.reserved_book_id = book_pool.book_id "
                           "WHERE reservations.reserved_book_id = %s;")
                    self.cursor.execute(sql, (book_id_text,))
                    book_is_reserved = self.cursor.fetchone()
                    if book_is_reserved[0] == 0:
                        print("Rezervasyon Yapıldı")
                        sql = "INSERT INTO reservations (reserved_book_id, reserved_user_id) VALUES (%s, %s)"
                        self.cursor.execute(sql, (book_id_text, entered_id,))
                        self.db_connection.commit()
                        sql = ("SELECT reserve_id FROM reservations "
                               "WHERE reserved_book_id = %s AND reserved_user_id = %s")
                        self.cursor.execute(sql, (book_id_text, entered_id))
                        queue_no = self.cursor.fetchone()
                        self.q.appendleft(queue_no)

                    else:
                        sql = "INSERT INTO reservations (reserved_book_id, reserved_user_id) VALUES (%s, %s)"
                        self.cursor.execute(sql, (book_id_text, entered_id,))
                        self.db_connection.commit()
                        sql = ("SELECT reserve_id FROM reservations WHERE reserved_book_id = %s "
                               "ORDER BY reserve_date ASC")
                        self.cursor.execute(sql, (book_id_text,))
                        for index, (reserve_id,) in enumerate(self.cursor):
                            self.q.append(reserve_id)
                            self.q_index.append(index + 1)
                        print("Rezervasyon Sıraya Alındı")
                        for queue_no in self.q_index:
                            reserve_no_list = list(self.q)

                            sql = "UPDATE reservations SET queue_no = %s WHERE reserve_id = %s"
                            self.cursor.execute(sql, (queue_no, reserve_no_list[queue_no - 1],))
                            self.db_connection.commit()
                except Error as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Rezervasyon Yapılamadı!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                    msg.setText("Hata Açıklaması: {}".format(str(e)))
                    msg.exec_()

                msg = QMessageBox()
                msg.setWindowTitle('Rezervasyon')
                text = 'Rezervasyonunuz oluşturuldu.'
                msg.setText(text)
                msg.setIcon(QMessageBox.Information)
                self.icon = QtGui.QIcon()
                self.icon.addPixmap(QtGui.QPixmap('../icons/checkMark.jpg'))
                msg.setWindowIcon(self.icon)
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Kitap seçimi yapınız.")
            msg.exec_()

    # Rezervasyon iptal butonu fonksiyonu
    def cancelReservationClick(self, entered_id):
        print('Rezervasyonu İptal Etme Butonuna Tıklandı.')
        msg = QMessageBox().question(self, "Rezervasyon İptali", "İptal etmek istediğinize emin misiniz?",
                                     QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:
            current_book = self.myReservationsTable.currentRow()
            book_name_column_index = 0
            book_name = self.myReservationsTable.item(current_book, book_name_column_index)
            book_name_text = book_name.text()
            try:
                sql = ("DELETE FROM reservations WHERE reserved_book_id = "
                       "(SELECT book_id FROM book_pool WHERE book_name = %s) "
                       "AND reserved_user_id = %s")
                self.cursor.execute(sql, (book_name_text, entered_id,))
                self.db_connection.commit()
                self.myReservationsTable.removeRow(current_book)
                print("Rezervasyon Silindi")
            except Error as e:
                msg = QMessageBox()
                msg.setWindowTitle("Rezervasyon İptal Edilemedi!")
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                msg.setText("Hata Açıklaması: {}".format(str(e)))
                msg.exec_()
        else:
            print("Hayır a basıldı")

    # Kitaplar Arama Algoritması:
    def booksSearchClick(self):
        search_text = self.lineEdit.text().lower()
        selected_column = self.booksTable.currentColumn()
        for i in range(self.booksTable.rowCount()):
            item = self.booksTable.item(i, selected_column)
            if item and search_text in item.text().lower():
                self.booksTable.setRowHidden(i, False)
            else:
                self.booksTable.setRowHidden(i, True)

    # Kitaplarım Arama Algoritması:
    def myBooksSearchClick(self):
        search_text = self.lineEdit2.text().lower()
        selected_column = self.myBooksTable.currentColumn()
        for i in range(self.myBooksTable.rowCount()):
            item = self.myBooksTable.item(i, selected_column)
            if item and search_text in item.text().lower():
                self.myBooksTable.setRowHidden(i, False)
            else:
                self.myBooksTable.setRowHidden(i, True)

    # Hepsini Göster Butonu Fonksiyonu (Kitaplar)
    def showAllClick(self):
        for i in range(self.booksTable.rowCount()):
            self.booksTable.setRowHidden(i, False)

    # Hepsini Göster Butonu Fonksiyonu 2 (Kitaplarım)
    def showAllClick2(self):
        for i in range(self.myBooksTable.rowCount()):
            self.myBooksTable.setRowHidden(i, False)

    def showDetailsClick(self):
        print('Ayrıntıları Göster Butonuna Tıklandı.')
        current_book = self.booksTable.currentRow()
        if current_book != -1:
            current_data = []
            for column in range(self.booksTable.columnCount()):
                datas = self.booksTable.item(current_book, column)
                if datas is not None:
                    current_data.append(datas.text())
                else:
                    current_data.append('')
            self.start = show_Info(self.db_connection, self.cursor, current_data)
            self.start.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Lütfen kitap seçiniz.")
            msg.exec_()
    def showDetailsClick2(self):
        print('Ayrıntıları Göster Butonuna Tıklandı.')
        current_book = self.myBooksTable.currentRow()
        book_id = self.myBooksTable.item(current_book, 1)
        if current_book != -1:
            self.start = show_Info(self.db_connection, self.cursor, book_id.text())
            self.start.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kitap Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Lütfen kitap seçiniz.")
            msg.exec_()

    # Şifre göster butonu fonksiyonu
    def togglePasswordVisibility(self):
        if self.birthEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.birthEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.birthEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    # İsimlendirme Fonksiyonu
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi"))
        self.welcomeLabel.setText(_translate("MainWindow", "Hoş Geldiniz!"))

        # Menü Bar
        self.booksButton.setText(_translate("MainWindow", "Kitaplar"))
        self.myBooksButton.setText(_translate("MainWindow", "Kitaplarım"))
        self.myReservations.setText(_translate('MainWindow', 'Rezervasyonlarım'))
        self.profileButton.setText(_translate("MainWindow", "Profil"))
        self.logoutButton.setText(_translate("MainWindow", "Çıkış Yap"))
        self.exitButton.setText(_translate("MainWindow", "Uygulamayı Kapat"))

        # Kitaplar
        self.takeBookButton.setText(_translate("MainWindow", "Kitabı Al"))
        self.searchLabel.setText(_translate("MainWindow", "Arama: "))
        self.booksLabel.setText(_translate('MainWindow', 'Kitaplar'))
        self.reservationButton.setText(_translate('MainWindow', 'Rezerve Et'))

        # Kitaplarım
        self.leaveBookButton.setText(_translate("MainWindow", "Kitabı Bırak"))
        self.searchLabel2.setText(_translate("MainWindow", "Arama: "))
        self.myBooksLabel.setText(_translate('MainWindow', 'Kitaplarım'))

        self.profileLabel.setText(_translate("MainWindow", "Profiliniz"))
        self.profileEditButton.setText(_translate("MainWindow", "Düzenle"))
        self.addressLabel.setText(_translate("MainWindow", "Adres: "))
        self.tcNoLabel.setText(_translate("MainWindow", "Kimlik No:"))
        self.phoneNoLabel.setText(_translate("MainWindow", "Telefon Numarası: "))
        self.surnameLabel.setText(_translate("MainWindow", "Soyad:"))
        self.nameLabel.setText(_translate("MainWindow", "İsim:"))
        self.idLabel.setText(_translate("MainWindow", "ID :"))
        self.birthLabel.setText(_translate("MainWindow", "Şifre:"))
        self.profileSaveButton.setText(_translate('MainWindow', 'Kaydet'))