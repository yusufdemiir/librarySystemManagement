from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QIcon
from mysql.connector import Error

class admin_Main_Window(QMainWindow):
    def __init__(self, db_connection, entered_id):
        super().__init__()
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

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
        self.welcomeLabel.setGeometry(QtCore.QRect(190, 440, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setObjectName("welcomeLabel")

        # Kitap Yönetimi Frame
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
        self.booksLabel.setObjectName("booksLabel")
        self.booksTable = QtWidgets.QTableWidget(self.booksFrame)
        self.booksTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.booksTable.setObjectName("booksTable")
        self.booksTable.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.deleteBookButton = QtWidgets.QPushButton(self.booksFrame)
        self.deleteBookButton.setGeometry(QtCore.QRect(470, 470, 111, 31))
        self.deleteBookButton.setObjectName("deleteBookButton")
        self.addBookButton = QtWidgets.QPushButton(self.booksFrame)
        self.addBookButton.setGeometry(QtCore.QRect(359, 470, 111, 31))
        self.addBookButton.setObjectName('addBookButton')
        self.widget = QtWidgets.QWidget(self.booksFrame)
        self.widget.setGeometry(QtCore.QRect(230, 10, 351, 87))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(50, 0, 0, 0)
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

        # Kullanıcı Yönetimi Frame
        self.userManagementFrame = QtWidgets.QFrame(self.centralwidget)
        self.userManagementFrame.setEnabled(True)
        self.userManagementFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.userManagementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userManagementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userManagementFrame.setObjectName("userManagemenetFrame")
        self.userManagementLabel = QtWidgets.QLabel(self.userManagementFrame)
        self.userManagementLabel.setGeometry(QtCore.QRect(20, 0, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.userManagementLabel.setFont(font)
        self.userManagementLabel.setObjectName("userManagementLabel")
        self.userTable = QtWidgets.QTableWidget(self.userManagementFrame)
        self.userTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.userTable.setObjectName("userTable")
        self.userTable.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.addUserButton = QtWidgets.QPushButton(self.userManagementFrame)
        self.addUserButton.setGeometry(QtCore.QRect(359, 470, 111, 31))
        self.addUserButton.setObjectName("addUserButton")
        self.deleteUserButton = QtWidgets.QPushButton(self.userManagementFrame)
        self.deleteUserButton.setGeometry(QtCore.QRect(470, 470, 111, 31))
        self.deleteUserButton.setObjectName('deleteUserButton')
        self.showInfoButton = QtWidgets.QPushButton(self.userManagementFrame)
        self.showInfoButton.setGeometry(QtCore.QRect(248, 470, 111, 31))
        self.showInfoButton.setObjectName("showInfoButton")
        self.widget = QtWidgets.QWidget(self.userManagementFrame)
        self.widget.setGeometry(QtCore.QRect(230, 10, 351, 87))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(90, 0, 0, 0)
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
        self.searchButton2 = QtWidgets.QPushButton(self.widget)
        self.searchButton2.setText("")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('../icons/search-icon.jpg'))
        self.searchButton2.setIcon(self.icon)
        self.searchButton2.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton2)
        self.showAll2 = QtWidgets.QPushButton(self.userManagementFrame)
        self.showAll2.setText('Hepsini Göster')
        self.showAll2.setGeometry(QtCore.QRect(2, 470, 90, 31, ))
        self.userManagementFrame.hide()

        # Rezervasyonlarım Frame
        self.myReservationsFrame = QtWidgets.QFrame(self.centralwidget)
        self.myReservationsFrame.setEnabled(True)
        self.myReservationsFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.myReservationsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.myReservationsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.myReservationsFrame.setObjectName("myBooksFrame")
        self.reservationsLable = QtWidgets.QLabel(self.myReservationsFrame)
        self.reservationsLable.setGeometry(QtCore.QRect(20, 0, 250, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.reservationsLable.setFont(font)
        self.reservationsLable.setObjectName("welcomeLabel")
        self.reservationsLable.setText('Rezervasyonlar')
        self.myReservationsTable = QtWidgets.QTableWidget(self.myReservationsFrame)
        self.myReservationsTable.setGeometry(QtCore.QRect(2, 75, 571, 379))
        self.myReservationsTable.setObjectName("myBooksTable")
        self.myReservationsTable.setEditTriggers(QTableWidget.NoEditTriggers)
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
        self.booksManagement = QtWidgets.QPushButton(self.widget)
        self.booksManagement.setObjectName("booksManagement")
        self.verticalLayout.addWidget(self.booksManagement)
        self.userManagementButton = QtWidgets.QPushButton(self.widget)
        self.userManagementButton.setObjectName("user")
        self.verticalLayout.addWidget(self.userManagementButton)
        self.reservationsButton = QtWidgets.QPushButton(self.widget)
        self.verticalLayout.addWidget(self.reservationsButton)
        self.reservationsButton.setText('Rezervasyonlar')
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
        self.booksManagement.clicked.connect(self.booksManagementClick)
        self.userManagementButton.clicked.connect(self.userManagementClick)
        self.profileButton.clicked.connect(self.profileClick)
        self.logoutButton.clicked.connect(self.logoutClick)
        self.profileEditButton.clicked.connect(self.profileEditClick)
        self.profileSaveButton.clicked.connect(lambda: self.profileSaveClick(entered_id))
        self.addBookButton.clicked.connect(self.addBookClick)
        self.deleteBookButton.clicked.connect(self.deleteBookClick)
        self.addUserButton.clicked.connect(self.addUserClick)
        self.deleteUserButton.clicked.connect(self.deleteUserClick)
        self.showInfoButton.clicked.connect(self.showInfoClick)
        self.searchButton.clicked.connect(self.booksSearchClick)
        self.searchButton2.clicked.connect(self.userSearchClick)
        self.showAll.clicked.connect(self.showAllClick)
        self.showAll2.clicked.connect(self.showAllClick2)
        self.showDetails.clicked.connect(self.showDetailsClick)
        self.reservationsButton.clicked.connect(self.reservationsButtonClick)
        self.showPasswordButton.clicked.connect(self.togglePasswordVisibility)
        self.exitButton.clicked.connect(self.closeApplicationClick)

    # Kitap yönetimi butonu fonskiyonu:
    def booksManagementClick(self):
        print('Kitaplar Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.userManagementFrame.hide()
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
    def userManagementClick(self):
        print('Kitaplarım Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.profileFrame.hide()
        self.myReservationsFrame.hide()
        self.userManagementFrame.show()
        self.load_users()

    # Kayıtlı kullanıcıları gösteren metot
    def load_users(self):
        try:
            sql = "SELECT * FROM users"
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            self.userTable.setRowCount(len(users))
            self.userTable.setColumnCount(8)

            for row_index, row_data in enumerate(users):
                for col_index, cell_data in enumerate(row_data):
                    self.userTable.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))
            table_header = ["ID", "Adı", "Soyadı", "Şifresi", "Rolü", "Telefon No", "Adres", "TC Kimlik No"]
            self.userTable.setHorizontalHeaderLabels(table_header)
        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Kullanıcılar Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Profil butonu fonksiyonu:
    def profileClick(self):
        print('Profil Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.userManagementFrame.hide()
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
        self.birthEdit.setReadOnly(False)
        self.idLineEdit.setReadOnly(False)
        self.checkLabel.hide()
    
    # Kaydetme butonu fonksiyonu
    def profileSaveClick(self, entered_id):
        print('Profili Kaydet Butonuna Tıklandı.')
        self.idLineEdit.setReadOnly(True)
        self.birthEdit.setReadOnly(True)
        self.nameLineEdit.setReadOnly(True)
        self.surnameEditLine.setReadOnly(True)
        self.phoneNoEditLine.setReadOnly(True)
        self.addressEdit.setReadOnly(True)
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

    # Kitap ekleme butonu fonksiyonu
    def addBookClick(self):
        print('Kitap Ekleme Butonuna Tıklandı')
        from addBookWindow import add_Book_Window
        self.startAddBookWindow = add_Book_Window(self.db_connection, self.cursor)
        self.startAddBookWindow.show()
        
    # Kitap silme butonu fonksiyonu
    def deleteBookClick(self):
        print('Kitap Silme Butonuna Tıklandı.')
        current_item = self.booksTable.currentRow()
        if current_item != -1:
            book_id_index = self.booksTable.item(current_item, 0)
            book_id = book_id_index.text()
            msg = QMessageBox().question(self, "Kitap Silme", "Silmek istediğinize emin misiniz?",
                                         QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox().Yes:
                try:
                    sql = "DELETE FROM book_pool WHERE book_id = %s"
                    self.cursor.execute(sql, (book_id,))
                    self.db_connection.commit()
                    self.booksTable.removeRow(current_item)
                    print("Kitap silindi")
                except Error as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Kitap Silinemedi!")
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

    #Kullanıcı Ekleme butonu fonksiyonu
    def addUserClick(self):
        print('Kullanıcı Ekleme Butonuna Tıklandı')
        from addUserWindow import add_User_Window
        self.startAddUserWindow = add_User_Window(self.db_connection, self.cursor)
        self.startAddUserWindow.show()
    
    #Kullanıcı Silme butonu fonksiyonu
    def deleteUserClick(self):
        print('Kullanıcı Silme Butonuna Tıklandı')
        current_item = self.userTable.currentRow()
        if current_item != -1:
            user_id_index = self.userTable.item(current_item, 0)
            user_id = user_id_index.text()

            msg = QMessageBox().question(self, "Kullanıcı Silme", "Silmek istediğinize emin misiniz?",
                                         QMessageBox.Yes | QMessageBox.No)
            if msg == QMessageBox.Yes:
                try:
                    sql = "DELETE FROM users WHERE user_id = %s"
                    self.cursor.execute(sql, (user_id,))
                    self.db_connection.commit()
                    self.userTable.removeRow(current_item)
                    print("Kullanıcı Silindi")
                except Error as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Kullanıcı Silinemedi!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowIcon(QIcon("../icons/redXicon.png"))
                    msg.setText("Hata Açıklaması: {}".format(str(e)))
                    msg.exec_()
            else:
                print("Hayır a basıldı")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Kullanıcı Seçilmedi!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Kullanıcı seçimi yapınız.")
            msg.exec_()

    # Bilgi gösterme butonu fonksiyonu
    def showInfoClick(self):
        print('Bilgi Gösterme Butonuna Tıklandı.')
        from showUserInfo import show_User_Info
        current_user = self.userTable.currentRow()
        if current_user != -1:
            current_data = []
            for column in range(self.userTable.columnCount()):
                datas = self.userTable.item(current_user, column)
                if datas is not None:
                    current_data.append(datas.text())
                else:
                    current_data.append('')
            self.start = show_User_Info(current_data)
            self.start.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Bilgi Sayfası Açılamadı!")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
            msg.setText("Bilgiler açılamadı. Tekrar deneyiniz.")
            msg.exec_()

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
    def userSearchClick(self):
        search_text = self.lineEdit2.text().lower()
        selected_column = self.userTable.currentColumn()
        for i in range(self.userTable.rowCount()):
            item = self.userTable.item(i, selected_column)
            if item and search_text in item.text().lower():
                self.userTable.setRowHidden(i, False)
            else:
                self.userTable.setRowHidden(i, True)

    # Hepsini Göster Butonu Fonksiyonu
    def showAllClick(self):
        for i in range(self.booksTable.rowCount()):
            self.booksTable.setRowHidden(i, False)

    def showAllClick2(self):
        for i in range(self.userTable.rowCount()):
            self.userTable.setRowHidden(i, False)

    # Detay Gösterme Butonu Fonksiyonu
    def showDetailsClick(self):
        from showInfo import show_Info
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

    # Rezervasyonlar Butonu Fonksiyonu
    def reservationsButtonClick(self):
        print('Rezervasyonlar Butonuna Tıklandı.')
        self.welcomeFrame.hide()
        self.booksFrame.hide()
        self.userManagementFrame.hide()
        self.profileFrame.hide()
        self.myReservationsFrame.show()
        try:
            sql = ("SELECT book_name FROM book_pool WHERE book_id "
                   "IN (SELECT DISTINCT reserved_book_id FROM reservations)")
            self.cursor.execute(sql)
            book_names = self.cursor.fetchall()
            self.myReservationsTable.setRowCount(len(book_names))
            self.myReservationsTable.setColumnCount(3)

            for row_index, row_data in enumerate(book_names):
                cell_data = row_data[0]
                self.myReservationsTable.setItem(row_index, 0, QTableWidgetItem(str(cell_data)))

            table_header = ["Kitap Adı", "Kitap Kimde?", "Sıradaki Kim?"]
            self.myReservationsTable.setHorizontalHeaderLabels(table_header)

            sql = ("SELECT reserved_user_id FROM reservations WHERE reserved_book_id IN "
                   "(SELECT DISTINCT book_id FROM book_pool WHERE book_name = %s) ORDER BY reserve_date ASC LIMIT 1")
            for book_index, book in enumerate(book_names):
                self.cursor.execute(sql, (book[book_index],))
                id_ = self.cursor.fetchone()
                if id_ is None:
                    msg = QMessageBox()
                    msg.setWindowTitle("Rezervasyon Yok!")
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
                    msg.setText("Bazı kitaplara ait rezervasyon kaydı bulunamadı.")
                    msg.exec_()
                else:
                    self.myReservationsTable.setItem(book_index, 2, QTableWidgetItem(str(id_[0])))

            sql = ("SELECT borrowed_user_id FROM borrowed_books WHERE borrowed_book_id IN "
                   "(SELECT DISTINCT book_id FROM book_pool WHERE book_name = %s) AND return_date IS NULL")
            for book_index, book in enumerate(book_names):
                self.cursor.execute(sql, (book[book_index],))
                id_ = self.cursor.fetchone()
                if id_ is None:
                    msg = QMessageBox()
                    msg.setWindowTitle("Kitap Alınmamış!")
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowIcon(QIcon("../icons/search-icon.jpg"))
                    msg.setText("Bazı kitaplara ait alınma kaydı bulunamadı.")
                    msg.exec_()
                else:
                    self.myReservationsTable.setItem(book_index, 1, QTableWidgetItem(str(id_[0])))

        except Error as e:
            msg = QMessageBox()
            msg.setWindowTitle("Rezervasyonlar Yüklenemedi!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QIcon("../icons/redXicon.png"))
            msg.setText("Hata Açıklaması: {}".format(str(e)))
            msg.exec_()

    # Şifre göster butonu fonksiyonu
    def togglePasswordVisibility(self):
        if self.birthEdit.echoMode() == QtWidgets.QLineEdit.Password:
            self.birthEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.birthEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    # Uygulamayı Kapat Tuşu
    def closeApplicationClick(self):
        # Veritabanı bağlantısını kapatma
        if self.db_connection:
            self.cursor.close()
            self.db_connection.close()
            print("Veri tabanı bağlantısı kapatıldı")
            # Uygulamayı kapatma
        QApplication.quit()

    # İsimlendirme Fonksiyonu
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi - (Yönetici Paneli)"))
        self.welcomeLabel.setText(_translate("MainWindow", "Yönetici Paneli."))
        
        # Menü Bar
        self.booksManagement.setText(_translate("MainWindow", "Kitap Yönetimi"))
        self.userManagementButton.setText(_translate("MainWindow", "Kullanıcı Yönetimi"))
        self.profileButton.setText(_translate("MainWindow", "Profil"))
        self.logoutButton.setText(_translate("MainWindow", "Çıkış Yap"))
        self.exitButton.setText(_translate("MainWindow", "Uygulamayı Kapat"))
        
        # Kitap Yönetimi
        self.deleteBookButton.setText(_translate("MainWindow", "Kitap Sil"))
        self.addBookButton.setText(_translate('MainWindow', 'Kitap Ekle'))
        self.searchLabel.setText(_translate("MainWindow", "Arama: "))
        self.booksLabel.setText(_translate('MainWindow', 'Kayıtlı Kitaplar'))
        
        # Kullanıcı Yönetimi
        self.addUserButton.setText(_translate("MainWindow", "Kullanıcı Ekle"))
        self.deleteUserButton.setText(_translate('MainWindow', 'Kullanıcı Sil'))
        self.searchLabel2.setText(_translate("MainWindow", "Arama: "))
        self.userManagementLabel.setText(_translate('MainWindow', 'Kayıtlı Kullanıcılar'))
        self.showInfoButton.setText(_translate('MainWindow', 'Bilgileri Göster'))
        
        # Profil
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