from loginWindow import login_Window
from PyQt5.QtWidgets import QApplication

print("  ")
app = QApplication([])
start = login_Window()
start.show()
app.exec()
print("  ")