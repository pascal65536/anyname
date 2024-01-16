import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton
from PyQt5 import uic
from coffee_form import CoffeeForm

SCREEN_SIZE = [800, 600]


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.addButton.clicked.connect(self.openAddCoffeeForm)
        self.editButton.clicked.connect(self.openEditCoffeeForm)
        self.con = sqlite3.connect("coffee.sqlite")
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 600, *SCREEN_SIZE)
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

    def openAddCoffeeForm(self):
        self.addCoffeeForm = CoffeeForm()
        # self.addCoffeeForm.saveButton.clicked.connect(self.saveCoffee)
        # self.addCoffeeForm.cancelButton.clicked.connect(self.saveCoffee)
        self.addCoffeeForm.exec_()

    def openEditCoffeeForm(self):
        selectedRow = self.tableWidget.currentRow()
        if selectedRow >= 0:
            coffeeId = self.tableWidget.item(selectedRow, 0).text()
            # Получите данные о кофе из базы данных по coffeeId
            coffeeData = self.getCoffeeData(coffeeId)
            if coffeeData:
                self.editCoffeeForm = CoffeeForm()
                self.editCoffeeForm.saveButton.clicked.connect(self.saveCoffee)
                # Заполните поля формы данными о кофе
                self.editCoffeeForm.nameLineEdit.setText(coffeeData['name'])
                self.editCoffeeForm.descriptionTextEdit.setPlainText(coffeeData['description'])
                self.editCoffeeForm.priceSpinBox.setValue(coffeeData['price'])
                self.editCoffeeForm.exec_()
        else:
            # Предупреждение: нет выбранной строки в таблице
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec())
