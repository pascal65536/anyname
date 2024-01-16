from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class CoffeeForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setModal(True)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    modal_form = CoffeeForm()
    modal_form.exec_()
    sys.exit(app.exec_())


