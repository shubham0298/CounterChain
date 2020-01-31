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
        itemadd.resize(800, 600)
        itemadd.setMinimumSize(QtCore.QSize(800, 600))
        itemadd.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(itemadd)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 290, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 170, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 290, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(270, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setObjectName("add")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(440, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setObjectName("back")
        itemadd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(itemadd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("itemadd", "Add Item"))
        self.label_2.setText(_translate("itemadd", "Product ID:"))
        self.label_3.setText(_translate("itemadd", "Product name:"))
        self.add.setText(_translate("itemadd", "ADD"))
        self.back.setText(_translate("itemadd", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    itemadd = QtWidgets.QMainWindow()
    ui = Ui_itemadd()
    ui.setupUi(itemadd)
    itemadd.show()
    sys.exit(app.exec_())
