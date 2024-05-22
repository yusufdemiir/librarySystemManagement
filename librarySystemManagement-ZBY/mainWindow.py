from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class main_Window(QMainWindow):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 10, 21, 531))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(190, 90, 561, 311))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(552, 50, 201, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 420, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 55, 16))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 30, 141, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuBar1 = QtWidgets.QPushButton(self.widget)
        self.menuBar1.setObjectName("menuBar1")
        self.verticalLayout.addWidget(self.menuBar1)
        self.menuBar2 = QtWidgets.QPushButton(self.widget)
        self.menuBar2.setObjectName("menuBar2")
        self.verticalLayout.addWidget(self.menuBar2)
        self.menuBar3 = QtWidgets.QPushButton(self.widget)
        self.menuBar3.setObjectName("menuBar3")
        self.verticalLayout.addWidget(self.menuBar3)
        self.menuBar4 = QtWidgets.QPushButton(self.widget)
        self.menuBar4.setObjectName("menuBar4")
        self.verticalLayout.addWidget(self.menuBar4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
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
        
        self.menuBar4.clicked.connect(self.exitClick)
    
    def exitClick(self):
        from loginWindow import login_Window
        self.startLoginWindow = login_Window()
        self.startLoginWindow.show()
        self.close()
        if self.db_connection:
            self.db_connection.close()
            print("Veri tabanı bağlantısı kapatıldı.")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Kitabi Al"))
        self.label.setText(_translate("MainWindow", "Arama:"))
        self.menuBar1.setText(_translate("MainWindow", "Kitaplar"))
        self.menuBar2.setText(_translate("MainWindow", "Kitaplarim"))
        self.menuBar3.setText(_translate("MainWindow", "Profil"))
        self.menuBar4.setText(_translate("MainWindow", "çikiş Yap"))
        self.pushButton_5.setText(_translate("MainWindow", "Uygulamayi Kapat"))
