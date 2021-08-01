# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\GUI\configures.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConfiguresUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(634, 443)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.General = QtWidgets.QWidget()
        self.General.setObjectName("General")
        self.groupBox = QtWidgets.QGroupBox(self.General)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 191))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 191, 41))
        self.label.setObjectName("label")
        self.DriveFolderIDEdit = QtWidgets.QLineEdit(self.groupBox)
        self.DriveFolderIDEdit.setGeometry(QtCore.QRect(230, 30, 331, 21))
        self.DriveFolderIDEdit.setObjectName("DriveFolderIDEdit")
        self.SelectSaveFilePathButton = QtWidgets.QPushButton(self.groupBox)
        self.SelectSaveFilePathButton.setGeometry(QtCore.QRect(520, 70, 41, 21))
        self.SelectSaveFilePathButton.setObjectName("SelectSaveFilePathButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 121, 61))
        self.label_7.setObjectName("label_7")
        self.SaveFilePathEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SaveFilePathEdit.setGeometry(QtCore.QRect(210, 70, 291, 21))
        self.SaveFilePathEdit.setReadOnly(True)
        self.SaveFilePathEdit.setObjectName("SaveFilePathEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 91, 41))
        self.label_4.setObjectName("label_4")
        self.WorldNameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.WorldNameEdit.setGeometry(QtCore.QRect(270, 110, 291, 21))
        self.WorldNameEdit.setReadOnly(True)
        self.WorldNameEdit.setObjectName("WorldNameEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 101, 21))
        self.label_2.setObjectName("label_2")
        self.GamePresetComboBox = QtWidgets.QComboBox(self.groupBox)
        self.GamePresetComboBox.setGeometry(QtCore.QRect(450, 150, 111, 22))
        self.GamePresetComboBox.setObjectName("GamePresetComboBox")
        self.GamePresetComboBox.addItem("")
        self.GamePresetComboBox.addItem("")
        self.GamePresetComboBox.addItem("")
        self.GamePresetComboBox.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.General)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 310, 591, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 201, 41))
        self.label_5.setObjectName("label_5")
        self.TrayCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.TrayCheckBox.setGeometry(QtCore.QRect(550, 25, 16, 31))
        self.TrayCheckBox.setText("")
        self.TrayCheckBox.setObjectName("TrayCheckBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.General)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 591, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.NoBackupRadioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.NoBackupRadioButton.setGeometry(QtCore.QRect(470, 30, 81, 21))
        self.NoBackupRadioButton.setObjectName("NoBackupRadioButton")
        self.OldRadioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.OldRadioButton.setGeometry(QtCore.QRect(350, 30, 71, 21))
        self.OldRadioButton.setObjectName("OldRadioButton")
        self.TimeRadioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.TimeRadioButton.setGeometry(QtCore.QRect(220, 30, 71, 21))
        self.TimeRadioButton.setObjectName("TimeRadioButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.General, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 591, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 151, 21))
        self.label_8.setObjectName("label_8")
        self.EveryXMinutesEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.EveryXMinutesEdit.setGeometry(QtCore.QRect(502, 20, 71, 20))
        self.EveryXMinutesEdit.setObjectName("EveryXMinutesEdit")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Update Preference"))
        self.label.setText(_translate("Form", "Google Drive Folder ID (see URL)"))
        self.SelectSaveFilePathButton.setText(_translate("Form", "..."))
        self.label_7.setText(_translate("Form", "Local Save file path"))
        self.label_4.setText(_translate("Form", "World name"))
        self.label_2.setText(_translate("Form", "Game Preset"))
        self.GamePresetComboBox.setItemText(0, _translate("Form", "Valheim"))
        self.GamePresetComboBox.setItemText(1, _translate("Form", "Minecraft"))
        self.GamePresetComboBox.setItemText(2, _translate("Form", "Terraria"))
        self.GamePresetComboBox.setItemText(3, _translate("Form", "Diablo II"))
        self.groupBox_4.setTitle(_translate("Form", "Background "))
        self.label_5.setText(_translate("Form", "Minimize to system tray on close"))
        self.groupBox_3.setTitle(_translate("Form", "Backup"))
        self.NoBackupRadioButton.setText(_translate("Form", "No Backup"))
        self.OldRadioButton.setText(_translate("Form", ".old"))
        self.TimeRadioButton.setText(_translate("Form", "Time"))
        self.label_3.setText(_translate("Form", "Backup File Style"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), _translate("Form", "General"))
        self.groupBox_2.setTitle(_translate("Form", "periodical update"))
        self.label_8.setText(_translate("Form", "Updates every x minutes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Auto Update"))