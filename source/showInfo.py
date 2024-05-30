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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Table = QtWidgets.QTableWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(5, 5, 400, 300))
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(3)
        self.Table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table.setItem(0, 2, item)
        self.Table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        
        self.retranslateUI(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUI(self, showInfo):
        _translate = QtCore.QCoreApplication.translate
        showInfo.setWindowTitle(_translate("userAddWindow", "Kullanıcı Bilgileri"))