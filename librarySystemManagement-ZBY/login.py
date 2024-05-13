from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Giriş Ekranı")
        MainWindow.resize(1200, 800)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(470, 490, 221, 61))
        self.enterButton.setObjectName("enterButton")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 700, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enterButton.setText(_translate("MainWindow", "Giriş"))
        self.label.setText(_translate("MainWindow", "Yeni kullanıcı iseniz lütfen bir yönetici ile iletişime geçin."))
        self.userRadioButton.setText(_translate("MainWindow", "Ziyaretçi"))
        self.adminRadioButton.setText(_translate("MainWindow", "Yönetici"))
        self.idLabel.setText(_translate("MainWindow", "Ziyaretçi ID:"))
        self.passwordLabel.setText(_translate("MainWindow", "Şifre:"))
