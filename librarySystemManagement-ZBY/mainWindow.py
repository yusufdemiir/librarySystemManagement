from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon, QPixmap

class main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        
        
        #Kitaplar Frame
        self.booksFrame = QtWidgets.QFrame(self.centralwidget)
        self.booksFrame.setEnabled(True)
        self.booksFrame.setGeometry(QtCore.QRect(180, 20, 591, 511))
        self.booksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksFrame.setObjectName("booksFrame")
        self.tableView = QtWidgets.QTableView(self.booksFrame)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 561, 351))
        self.tableView.setObjectName("tableView")
        self.takeBookButton = QtWidgets.QPushButton(self.booksFrame)
        self.takeBookButton.setGeometry(QtCore.QRect(470, 450, 111, 31))
        self.takeBookButton.setObjectName("takeBookButton")
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
        self.searchIcon = QPixmap('search-icon.jpg')
        self.searchButton.setIcon(QIcon(self.searchIcon))
        self.searchButton.setIconSize(self.searchIcon.size())
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.booksFrame.hide()
        
        #Kitaplarım Frame
        
        #Profil Frame
        
        
        
    
    
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
        
        #Butonların Fonksiyonlar ile Bağlanması
        self.booksButton.clicked.connect(self.booksClick)
        self.myBooksButton.clicked.connect(self.myBooksClick)
        self.profileButton.clicked.connect(self.profileClick)
        self.logoutButton.clicked.connect(self.logoutClick)
        self.exitButton.clicked.connect(QApplication.instance().quit)
    
    
    
    #Kitaplar butonu fonskiyonu:
    def booksClick(self):
        print('Kitaplar Butonuna Tıklandı.')
        self.booksFrame.show()
    
    #Kitaplarım butonu fonksiyonu:
    def myBooksClick(self):
        print('Kitaplarım Butonuna Tıklandı.')
    
    #Profil butonu fonksiyonu:
    def profileClick(self):
        print('Profil Butonuna Tıklandı.')

    #Çıkış yapma butonu fonksiyonu
    def logoutClick(self):
        print('Çıkış Butonuna Tıklandı.')
        from loginWindow import login_Window
        self.startLoginWindow = login_Window()
        self.startLoginWindow.show()
        self.close()
        print('Giriş Ekranına Geçildi.')



    #İsimlendirme Fonksiyonu
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi"))
        self.takeBookButton.setText(_translate("MainWindow", "Kitabı Al"))
        self.booksButton.setText(_translate("MainWindow", "Kitaplar"))
        self.myBooksButton.setText(_translate("MainWindow", "Kitaplarım"))
        self.profileButton.setText(_translate("MainWindow", "Profil"))
        self.logoutButton.setText(_translate("MainWindow", "Çıkış Yap"))
        self.exitButton.setText(_translate("MainWindow", "Uygulamayı Kapat"))
        self.searchLabel.setText(_translate("MainWindow", "Arama: "))
