import sys
from frontPage import MySideBar
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

app = QApplication(sys.argv)

window = MySideBar()
  

window.show()
sys.exit(app.exec())


