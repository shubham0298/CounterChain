# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sell.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SellWindow(object):
    def setupUi(self, SellWindow):
        SellWindow.setObjectName("SellWindow")
        SellWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SellWindow.sizePolicy().hasHeightForWidth())
        SellWindow.setSizePolicy(sizePolicy)
        SellWindow.setMinimumSize(QtCore.QSize(1000, 800))
        SellWindow.setMaximumSize(QtCore.QSize(1000, 800))
        SellWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(85, 85, 127);\n"
"}\n"
"QLineEdit{    \n"
"    background-color: rgb(154, 154, 229);\n"
"}\n"
"QPushButton#homeButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton#sellConfirmButton{\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"QPushButton#resetButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"QPushButton#clearButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SellWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sellConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.sellConfirmButton.setGeometry(QtCore.QRect(350, 560, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sellConfirmButton.sizePolicy().hasHeightForWidth())
        self.sellConfirmButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sellConfirmButton.setFont(font)
        self.sellConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sellConfirmButton.setObjectName("sellConfirmButton")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 150, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.buyeridLE = QtWidgets.QLineEdit(self.centralwidget)
        self.buyeridLE.setGeometry(QtCore.QRect(440, 410, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buyeridLE.setFont(font)
        self.buyeridLE.setObjectName("buyeridLE")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setObjectName("label_2")
        self.pidLE = QtWidgets.QLineEdit(self.centralwidget)
        self.pidLE.setGeometry(QtCore.QRect(440, 310, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pidLE.setFont(font)
        self.pidLE.setObjectName("pidLE")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 310, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_6.setObjectName("label_6")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(570, 560, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setObjectName("resetButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(810, 310, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setObjectName("clearButton")
        SellWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SellWindow)
        self.statusbar.setObjectName("statusbar")
        SellWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(SellWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(SellWindow)
        QtCore.QMetaObject.connectSlotsByName(SellWindow)

    def retranslateUi(self, SellWindow):
        _translate = QtCore.QCoreApplication.translate
        SellWindow.setWindowTitle(_translate("SellWindow", "CounterChain - Sell Items"))
        self.sellConfirmButton.setText(_translate("SellWindow", "Confirm"))
        self.homeButton.setText(_translate("SellWindow", " Back"))
        self.label.setText(_translate("SellWindow", "Sell Items"))
        self.label_5.setText(_translate("SellWindow", "CounterChain"))
        self.label_2.setText(_translate("SellWindow", "Buyer ID:"))
        self.label_6.setText(_translate("SellWindow", "Product ID:"))
        self.resetButton.setText(_translate("SellWindow", "Reset"))
        self.clearButton.setText(_translate("SellWindow", "Clear PID"))
        self.actionExit.setText(_translate("SellWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SellWindow = QtWidgets.QMainWindow()
    ui = Ui_SellWindow()
    ui.setupUi(SellWindow)
    SellWindow.show()
    sys.exit(app.exec_())
