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
        self.tableWidget.setGeometry(QtCore.QRect(210, 240, 551, 441))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 700, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 211, 71))
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

        head1 = QtWidgets.QTableWidgetItem()
        head1.setText("Product ID")
        self.tableWidget.setHorizontalHeaderItem(0,head1)

        head2 = QtWidgets.QTableWidgetItem()
        head2.setText("Product Name")
        self.tableWidget.setHorizontalHeaderItem(1,head2)

        head3 = QtWidgets.QTableWidgetItem()
        head3.setText("Quantity")
        self.tableWidget.setHorizontalHeaderItem(2,head3)

        head4 = QtWidgets.QTableWidgetItem()
        head4.setText("Comment")
        self.tableWidget.setHorizontalHeaderItem(3,head4)

        self.retranslateUi(inventory)
        QtCore.QMetaObject.connectSlotsByName(inventory)

    def retranslateUi(self, inventory):
        _translate = QtCore.QCoreApplication.translate
        inventory.setWindowTitle(_translate("inventory", "Inventory"))
        self.label.setText(_translate("inventory", "Inventory"))
        self.pushButton.setText(_translate("inventory", "Back"))
        self.label_3.setText(_translate("inventory", "CounterChain"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory = QtWidgets.QMainWindow()
    ui = Ui_inventory()
    ui.setupUi(inventory)
    inventory.show()
    sys.exit(app.exec_())
