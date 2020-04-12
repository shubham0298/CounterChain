# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inventory(object):
    def setupUi(self, inventory):
        inventory.setObjectName("inventory")
        inventory.resize(1000, 800)
        inventory.setMinimumSize(QtCore.QSize(1000, 800))
        inventory.setMaximumSize(QtCore.QSize(1000, 800))
        inventory.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(inventory)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 150, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 240, 600, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/backbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 211, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setObjectName("label_3")
        inventory.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inventory)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        inventory.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inventory)
        self.statusbar.setObjectName("statusbar")
        inventory.setStatusBar(self.statusbar)

        self.retranslateUi(inventory)
        QtCore.QMetaObject.connectSlotsByName(inventory)

    def retranslateUi(self, inventory):
        _translate = QtCore.QCoreApplication.translate
        inventory.setWindowTitle(_translate("inventory", "Inventory"))
        self.label.setText(_translate("inventory", "Inventory"))
        self.pushButton.setText(_translate("inventory", " Back"))
        self.label_3.setText(_translate("inventory", "CounterChain"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory = QtWidgets.QMainWindow()
    ui = Ui_inventory()
    ui.setupUi(inventory)
    inventory.show()
    sys.exit(app.exec_())
