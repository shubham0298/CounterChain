# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receiveWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReceiveWindow(object):
    def setupUi(self, ReceiveWindow):
        ReceiveWindow.setObjectName("ReceiveWindow")
        ReceiveWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReceiveWindow.sizePolicy().hasHeightForWidth())
        ReceiveWindow.setSizePolicy(sizePolicy)
        ReceiveWindow.setMinimumSize(QtCore.QSize(1000, 800))
        ReceiveWindow.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setPointSize(12)
        ReceiveWindow.setFont(font)
        ReceiveWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(85, 85, 127);\n"
"}\n"
"QPushButton#homeButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton#rcvButton{\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton#rcvallButton{\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton#checkButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ReceiveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(375, 150, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.rcvButton = QtWidgets.QPushButton(self.centralwidget)
        self.rcvButton.setGeometry(QtCore.QRect(320, 670, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rcvButton.setFont(font)
        self.rcvButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rcvButton.setObjectName("rcvButton")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(860, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/backbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(30, 30))
        self.homeButton.setObjectName("homeButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 211, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_5.setObjectName("label_5")
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(740, 220, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkButton.setFont(font)
        self.checkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkButton.setObjectName("checkButton")
        self.rcvTable = QtWidgets.QTableWidget(self.centralwidget)
        self.rcvTable.setGeometry(QtCore.QRect(170, 320, 700, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rcvTable.sizePolicy().hasHeightForWidth())
        self.rcvTable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rcvTable.setFont(font)
        self.rcvTable.setStyleSheet("background-color: rgb(154, 154, 229);")
        self.rcvTable.setObjectName("rcvTable")
        self.rcvTable.setColumnCount(4)
        self.rcvTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.rcvTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rcvTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rcvTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.rcvTable.setHorizontalHeaderItem(3, item)
        self.rcvallButton = QtWidgets.QPushButton(self.centralwidget)
        self.rcvallButton.setGeometry(QtCore.QRect(600, 670, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rcvallButton.setFont(font)
        self.rcvallButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rcvallButton.setObjectName("rcvallButton")
        ReceiveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReceiveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        ReceiveWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReceiveWindow)
        self.statusbar.setObjectName("statusbar")
        ReceiveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReceiveWindow)
        QtCore.QMetaObject.connectSlotsByName(ReceiveWindow)

    def retranslateUi(self, ReceiveWindow):
        _translate = QtCore.QCoreApplication.translate
        ReceiveWindow.setWindowTitle(_translate("ReceiveWindow", "CounterChain - Receive Items"))
        self.label.setText(_translate("ReceiveWindow", "Receive Items"))
        self.rcvButton.setText(_translate("ReceiveWindow", "Confirm"))
        self.homeButton.setText(_translate("ReceiveWindow", " Back"))
        self.label_5.setText(_translate("ReceiveWindow", "CounterChain"))
        self.checkButton.setText(_translate("ReceiveWindow", "Refresh"))
        item = self.rcvTable.horizontalHeaderItem(0)
        item.setText(_translate("ReceiveWindow", "Seller ID"))
        item = self.rcvTable.horizontalHeaderItem(1)
        item.setText(_translate("ReceiveWindow", "Product ID"))
        item = self.rcvTable.horizontalHeaderItem(2)
        item.setText(_translate("ReceiveWindow", "Product Name"))
        item = self.rcvTable.horizontalHeaderItem(3)
        item.setText(_translate("ReceiveWindow", "Status"))
        self.rcvallButton.setText(_translate("ReceiveWindow", "Confirm All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReceiveWindow = QtWidgets.QMainWindow()
    ui = Ui_ReceiveWindow()
    ui.setupUi(ReceiveWindow)
    ReceiveWindow.show()
    sys.exit(app.exec_())
