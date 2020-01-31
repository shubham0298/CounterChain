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
        inventory.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(inventory)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(140, 60, 551, 401))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 490, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        inventory.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inventory)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        inventory.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inventory)
        self.statusbar.setObjectName("statusbar")
        inventory.setStatusBar(self.statusbar)

        head1 = QtWidgets.QTableWidgetItem();
        head1.setText("Product Info")
        self.tableWidget.setHorizontalHeaderItem(0,head1);

        head2 = QtWidgets.QTableWidgetItem();
        head2.setText("Product details")
        self.tableWidget.setHorizontalHeaderItem(1,head2);

        head3 = QtWidgets.QTableWidgetItem();
        head3.setText("Quantity")
        self.tableWidget.setHorizontalHeaderItem(2,head3);

        head4 = QtWidgets.QTableWidgetItem();
        head4.setText("Status")
        self.tableWidget.setHorizontalHeaderItem(3,head4);

        self.retranslateUi(inventory)
        QtCore.QMetaObject.connectSlotsByName(inventory)

    def retranslateUi(self, inventory):
        _translate = QtCore.QCoreApplication.translate
        inventory.setWindowTitle(_translate("inventory", "Inventory"))
        self.label.setText(_translate("inventory", "Inventory"))
        self.pushButton.setText(_translate("inventory", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory = QtWidgets.QMainWindow()
    ui = Ui_inventory()
    ui.setupUi(inventory)
    inventory.show()
    sys.exit(app.exec_())
