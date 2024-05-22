from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget


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
        self.pushButton = QtWidgets.QPushButton(self.booksFrame)
        self.pushButton.setGeometry(QtCore.QRect(470, 450, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.booksFrame)
        self.widget.setGeometry(QtCore.QRect(230, 10, 351, 87))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../librarySystemManagement/librarySystemManagement-ZBY/pic/search-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.booksFrame.hide()
        
        
    
    
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
        self.pushButton_5.clicked.connect(self.execClick)
        self.menuBar1.clicked.connect(self.booksClick)
    
    def exitClick(self):
        from loginWindow import login_Window
        self.startLoginWindow = login_Window()
        self.startLoginWindow.show()
        self.close()
    
    def execClick(self):
        QApplication.quit()
    
    def booksClick(self):
        self.booksFrame.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ZBY Kütüphane Sistemi"))
        self.pushButton.setText(_translate("MainWindow", "Kitabı Al"))
        
        self.menuBar1.setText(_translate("MainWindow", "Kitaplar"))
        self.menuBar2.setText(_translate("MainWindow", "Kitaplarım"))
        self.menuBar3.setText(_translate("MainWindow", "Profil"))
        self.menuBar4.setText(_translate("MainWindow", "Çıkış Yap"))
        self.pushButton_5.setText(_translate("MainWindow", "Uygulamayı Kapat"))
