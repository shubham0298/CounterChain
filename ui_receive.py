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
        ReceiveWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReceiveWindow.sizePolicy().hasHeightForWidth())
        ReceiveWindow.setSizePolicy(sizePolicy)
        ReceiveWindow.setMinimumSize(QtCore.QSize(800, 600))
        ReceiveWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(ReceiveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 780, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 110, 150, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.rcvNextButton = QtWidgets.QPushButton(self.centralwidget)
        self.rcvNextButton.setGeometry(QtCore.QRect(370, 490, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rcvNextButton.setFont(font)
        self.rcvNextButton.setObjectName("rcvNextButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 170, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 170, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.itemList = QtWidgets.QTextBrowser(self.centralwidget)
        self.itemList.setGeometry(QtCore.QRect(160, 210, 431, 251))
        self.itemList.setObjectName("itemList")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.homeButton.setObjectName("homeButton")
        ReceiveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReceiveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_2.setText(_translate("ReceiveWindow", "Seller ID"))
        self.rcvNextButton.setText(_translate("ReceiveWindow", "Confirm"))
        self.label_3.setText(_translate("ReceiveWindow", "Product Info"))
        self.label_4.setText(_translate("ReceiveWindow", "Status"))
        self.homeButton.setText(_translate("ReceiveWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReceiveWindow = QtWidgets.QMainWindow()
    ui = Ui_ReceiveWindow()
    ui.setupUi(ReceiveWindow)
    ReceiveWindow.show()
    sys.exit(app.exec_())
