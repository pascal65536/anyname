import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic


class CoffeeForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setModal(True)
        self.cancelButton.clicked.connect(self.reject)
        self.saveButton.clicked.connect(self.accept)
        self.line_edit_variety.textChanged.connect(self.text_changed)
        self.line_edit_roasting.textChanged.connect(self.text_changed)
        self.line_edit_ground.textChanged.connect(self.text_changed)
        self.line_edit_flavor.textChanged.connect(self.text_changed)
        self.line_edit_price.textChanged.connect(self.text_changed)
        self.line_edit_volume.textChanged.connect(self.text_changed)

    def text_changed(self):
        text_lst = [self.line_edit_variety.text(),
                    self.line_edit_roasting.text(),
                    self.line_edit_ground.text(),
                    self.line_edit_flavor.text(),
                    self.line_edit_price.text(),
                    self.line_edit_volume.text()]
        if text_lst.count(''):
            self.saveButton.setEnabled(False)
        else:
            self.saveButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    dialog = CoffeeForm()
    result = dialog.exec_()
    app.quit()
