# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sell.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SellWindow(object):
    def setupUi(self, SellWindow):
        SellWindow.setObjectName("SellWindow")
        SellWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SellWindow.sizePolicy().hasHeightForWidth())
        SellWindow.setSizePolicy(sizePolicy)
        SellWindow.setMinimumSize(QtCore.QSize(800, 600))
        SellWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(SellWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.productName = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productName.sizePolicy().hasHeightForWidth())
        self.productName.setSizePolicy(sizePolicy)
        self.productName.setIconSize(QtCore.QSize(14, 16))
        self.productName.setObjectName("productName")
        self.productName.addItem("")
        self.productName.addItem("")
        self.productName.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.productName)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.quantity = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantity.sizePolicy().hasHeightForWidth())
        self.quantity.setSizePolicy(sizePolicy)
        self.quantity.setObjectName("quantity")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.quantity)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.buyerID = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buyerID.sizePolicy().hasHeightForWidth())
        self.buyerID.setSizePolicy(sizePolicy)
        self.buyerID.setObjectName("buyerID")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buyerID)
        self.sellConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sellConfirmButton.sizePolicy().hasHeightForWidth())
        self.sellConfirmButton.setSizePolicy(sizePolicy)
        self.sellConfirmButton.setObjectName("sellConfirmButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sellConfirmButton)
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setObjectName("homeButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.homeButton)
        SellWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SellWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCounterChain = QtWidgets.QMenu(self.menubar)
        self.menuCounterChain.setObjectName("menuCounterChain")
        SellWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SellWindow)
        self.statusbar.setObjectName("statusbar")
        SellWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(SellWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuCounterChain.addAction(self.actionExit)
        self.menubar.addAction(self.menuCounterChain.menuAction())

        self.retranslateUi(SellWindow)
        QtCore.QMetaObject.connectSlotsByName(SellWindow)

    def retranslateUi(self, SellWindow):
        _translate = QtCore.QCoreApplication.translate
        SellWindow.setWindowTitle(_translate("SellWindow", "CounterChain - Sell Items"))
        self.label.setText(_translate("SellWindow", "Sell Items"))
        self.label_2.setText(_translate("SellWindow", "Product Name"))
        self.productName.setItemText(0, _translate("SellWindow", "Select Item"))
        self.productName.setItemText(1, _translate("SellWindow", "Drug 1"))
        self.productName.setItemText(2, _translate("SellWindow", "Drug 2"))
        self.label_4.setText(_translate("SellWindow", "Quantity"))
        self.label_3.setText(_translate("SellWindow", "Buyer ID"))
        self.sellConfirmButton.setText(_translate("SellWindow", "Confirm"))
        self.homeButton.setText(_translate("SellWindow", "Home"))
        self.menuCounterChain.setTitle(_translate("SellWindow", "CounterChain"))
        self.actionExit.setText(_translate("SellWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SellWindow = QtWidgets.QMainWindow()
    ui = Ui_SellWindow()
    ui.setupUi(SellWindow)
    SellWindow.show()
    sys.exit(app.exec_())
