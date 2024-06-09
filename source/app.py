from loginWindow import login_Window
from PyQt5.QtWidgets import QApplication

app = QApplication([])
start = login_Window()
start.show()
app.exec()