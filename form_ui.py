# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 220)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_variety = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_variety.setObjectName("label_variety")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_variety)
        self.line_edit_variety = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_variety.setObjectName("line_edit_variety")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_variety)
        self.label_roasting = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_roasting.setObjectName("label_roasting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_roasting)
        self.line_edit_roasting = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_roasting.setObjectName("line_edit_roasting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_edit_roasting)
        self.label_ground = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ground.setObjectName("label_ground")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_ground)
        self.line_edit_ground = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_ground.setObjectName("line_edit_ground")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_ground)
        self.label_flavor = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_flavor.setObjectName("label_flavor")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_flavor)
        self.line_edit_flavor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_flavor.setObjectName("line_edit_flavor")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_edit_flavor)
        self.label_price = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_price.setObjectName("label_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_price)
        self.line_edit_price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_price.setObjectName("line_edit_price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_edit_price)
        self.label_volume = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_volume.setObjectName("label_volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_volume)
        self.line_edit_volume = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_volume.setObjectName("line_edit_volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_edit_volume)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(306, 190, 81, 23))
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(220, 190, 80, 23))
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Кофейный редактор"))
        self.label_variety.setText(_translate("Form", "Variety name"))
        self.label_roasting.setText(_translate("Form", "Degree of roasting"))
        self.label_ground.setText(_translate("Form", "Ground/in grains"))
        self.label_flavor.setText(_translate("Form", "Flavor description"))
        self.label_price.setText(_translate("Form", "Price"))
        self.label_volume.setText(_translate("Form", "Package volume"))
        self.saveButton.setText(_translate("Form", "Окей"))
        self.cancelButton.setText(_translate("Form", "Отмена"))