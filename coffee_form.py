from form_ui import Ui_Form
from PyQt5.QtWidgets import QDialog, QApplication


class CoffeeForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.saveButton.clicked.connect(self.accept)
        self.ui.line_edit_variety.textChanged.connect(self.text_changed)
        self.ui.line_edit_roasting.textChanged.connect(self.text_changed)
        self.ui.line_edit_ground.textChanged.connect(self.text_changed)
        self.ui.line_edit_flavor.textChanged.connect(self.text_changed)
        self.ui.line_edit_price.textChanged.connect(self.text_changed)
        self.ui.line_edit_volume.textChanged.connect(self.text_changed)

    def text_changed(self):
        text_lst = [self.ui.line_edit_variety.text(),
                    self.ui.line_edit_roasting.text(),
                    self.ui.line_edit_ground.text(),
                    self.ui.line_edit_flavor.text(),
                    self.ui.line_edit_price.text(),
                    self.ui.line_edit_volume.text()]
        if text_lst.count(''):
            self.ui.saveButton.setEnabled(False)
        else:
            self.ui.saveButton.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    dialog = CoffeeForm()
    result = dialog.exec_()
    app.quit()
