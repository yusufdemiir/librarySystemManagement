from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidget
from PyQt5.QtGui import QIcon, QPixmap

class show_Info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("showInfo")
        self.resize(600, 400)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('icons/logo.jpeg'))
        self.setWindowIcon(self.icon)
        self.setWindowTitle('Kullanıcı Bilgisi')
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(250,340,100,28))
        self.Label.setObjectName('Label')
        self.Label.setText('Yusuf Demir kişisinde bulunan kitaplar')