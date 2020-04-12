# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutus.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutus(object):
    def setupUi(self, aboutus):
        aboutus.setObjectName("aboutus")
        aboutus.resize(800, 600)
        aboutus.setMinimumSize(QtCore.QSize(800, 600))
        aboutus.setMaximumSize(QtCore.QSize(800, 600))
        aboutus.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(aboutus)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(360, 490, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("backButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 190, 701, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        aboutus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(aboutus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        aboutus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(aboutus)
        self.statusbar.setObjectName("statusbar")
        aboutus.setStatusBar(self.statusbar)

        self.retranslateUi(aboutus)
        QtCore.QMetaObject.connectSlotsByName(aboutus)

    def retranslateUi(self, aboutus):
        _translate = QtCore.QCoreApplication.translate
        aboutus.setWindowTitle(_translate("aboutus", "About Us"))
        self.label.setText(_translate("aboutus", "About CounterChain"))
        self.backButton.setText(_translate("aboutus", "OK"))
        self.textBrowser.setHtml(_translate("aboutus", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">    The main goal behind developing CounterChain is to detect Counterfeit Drugs in the supply market. CounterChain is mainly based on blockchain technology. Using blockchain, a transaction can be verified and be visible to all the entities in supply chain, thus increasing the transparency and reducing additional expenses of using third party verifiers.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">    CounterChain Software provides three options of registration to users as Manufacturer, Distributer or Retailer. User\'s required to have license no. to register as per their corresponding role in supply chain. User\'s can use services only after the application is accepted by the administrator.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutus = QtWidgets.QMainWindow()
    ui = Ui_aboutus()
    ui.setupUi(aboutus)
    aboutus.show()
    sys.exit(app.exec_())
