from main_ui import Ui_MainWindow
import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PyQt5 import uic
from coffee_form import CoffeeForm

SCREEN_SIZE = [800, 600]


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.openAddCoffeeForm)
        self.ui.editButton.clicked.connect(self.openEditCoffeeForm)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 600, *SCREEN_SIZE)
        self.display_data()

    def create_data(self, variety, roasting, ground, flavor, price, volume):
        cur = self.con.cursor()
        query = f"INSERT into COFFEE(variety, roasting, ground, flavor, price, volume) "
        query += f"VALUES ({variety}, {roasting}, {ground}, {flavor}, {price}, {volume})"
        cur.execute(query)
        self.con.commit()

    def update_data(self, coffee_id, variety, roasting, ground, flavor, price, volume):
        cur = self.con.cursor()
        query = f"UPDATE coffee SET variety = '{variety}', roasting = '{roasting}', ground = '{ground}', "
        query += f"flavor = '{flavor}', price = '{price}', volume = '{volume}' WHERE id == {coffee_id}"
        cur.execute(query)
        self.con.commit()

    def display_data(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM coffee")
        result = cur.fetchall()
        self.ui.tableWidget.setRowCount(len(result))
        if not result:
            self.ui.statusbar.showMessage("Ничего не нашлось")
            return
        else:
            self.ui.statusbar.showMessage("OK")
        self.ui.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def openAddCoffeeForm(self):
        self.addCoffeeForm = CoffeeForm()
        self.addCoffeeForm.exec_()
        if self.addCoffeeForm.result() == QDialog.Accepted:
            create_lst = []
            create_lst.append(self.addCoffeeForm.ui.line_edit_variety.text())
            create_lst.append(self.addCoffeeForm.ui.line_edit_roasting.text())
            create_lst.append(self.addCoffeeForm.ui.line_edit_ground.text())
            create_lst.append(self.addCoffeeForm.ui.line_edit_flavor.text())
            create_lst.append(self.addCoffeeForm.ui.line_edit_price.text())
            create_lst.append(self.addCoffeeForm.ui.line_edit_volume.text())
            self.create_data(*create_lst)
            self.display_data()

    def openEditCoffeeForm(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row < 0:
            return
        coffee_id = self.ui.tableWidget.item(selected_row, 0).text()
        self.editCoffeeForm = CoffeeForm()
        self.editCoffeeForm.ui.line_edit_variety.setText(self.ui.tableWidget.item(selected_row, 1).text())
        self.editCoffeeForm.ui.line_edit_roasting.setText(self.ui.tableWidget.item(selected_row, 2).text())
        self.editCoffeeForm.ui.line_edit_ground.setText(self.ui.tableWidget.item(selected_row, 3).text())
        self.editCoffeeForm.ui.line_edit_flavor.setText(self.ui.tableWidget.item(selected_row, 4).text())
        self.editCoffeeForm.ui.line_edit_price.setText(self.ui.tableWidget.item(selected_row, 5).text())
        self.editCoffeeForm.ui.line_edit_volume.setText(self.ui.tableWidget.item(selected_row, 6).text())
        self.editCoffeeForm.exec_()
        if self.editCoffeeForm.result() == QDialog.Accepted:
            update_lst = [coffee_id]
            update_lst.append(self.editCoffeeForm.ui.line_edit_variety.text())
            update_lst.append(self.editCoffeeForm.ui.line_edit_roasting.text())
            update_lst.append(self.editCoffeeForm.ui.line_edit_ground.text())
            update_lst.append(self.editCoffeeForm.ui.line_edit_flavor.text())
            update_lst.append(self.editCoffeeForm.ui.line_edit_price.text())
            update_lst.append(self.editCoffeeForm.ui.line_edit_volume.text())
            self.update_data(*update_lst)
            self.display_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Coffe()
    ex.show()
    sys.exit(app.exec())
