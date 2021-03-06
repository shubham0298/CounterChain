# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemadd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_itemadd(object):
    def setupUi(self, itemadd):
        itemadd.setObjectName("itemadd")
        itemadd.resize(1000, 800)
        itemadd.setMinimumSize(QtCore.QSize(1000, 800))
        itemadd.setMaximumSize(QtCore.QSize(1000, 800))
        itemadd.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(itemadd)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 150, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 320, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 420, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setObjectName("label_3")
        self.pidLE = QtWidgets.QLineEdit(self.centralwidget)
        self.pidLE.setGeometry(QtCore.QRect(480, 320, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pidLE.setFont(font)
        self.pidLE.setObjectName("pidLE")
        self.pnameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.pnameLE.setGeometry(QtCore.QRect(480, 420, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pnameLE.setFont(font)
        self.pnameLE.setObjectName("pnameLE")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(450, 560, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setObjectName("addButton")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(860, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/backbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(30, 30))
        self.back.setObjectName("back")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 0, 211, 71))
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
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_4.setObjectName("label_4")
        itemadd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(itemadd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        itemadd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(itemadd)
        self.statusbar.setObjectName("statusbar")
        itemadd.setStatusBar(self.statusbar)

        self.retranslateUi(itemadd)
        QtCore.QMetaObject.connectSlotsByName(itemadd)

    def retranslateUi(self, itemadd):
        _translate = QtCore.QCoreApplication.translate
        itemadd.setWindowTitle(_translate("itemadd", "Add Item"))
        self.label.setText(_translate("itemadd", "Register Product"))
        self.label_2.setText(_translate("itemadd", "Product ID:"))
        self.label_3.setText(_translate("itemadd", "Product name:"))
        self.addButton.setText(_translate("itemadd", "Register"))
        self.back.setText(_translate("itemadd", " Back"))
        self.label_4.setText(_translate("itemadd", "CounterChain"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemadd = QtWidgets.QMainWindow()
    ui = Ui_itemadd()
    ui.setupUi(itemadd)
    itemadd.show()
    sys.exit(app.exec_())
