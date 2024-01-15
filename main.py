import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


SCREEN_SIZE = [800, 480]


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 480, *SCREEN_SIZE)
        self.display_data()

    def display_data(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM coffee")
        result = cur.fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage("Ничего не нашлось")
            return
        else:
            self.statusBar().showMessage("OK")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec())
