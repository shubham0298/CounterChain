import sys
from MCHelper import MCClient, MCNodeCreator
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_DashboardWindow
from ui_sell import Ui_SellWindow
from ui_receive import Ui_ReceiveWindow

class MainWindow(QtWidgets.QMainWindow, Ui_DashboardWindow):

    open_sell = QtCore.pyqtSignal()
    open_receive = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.sellButton.clicked.connect(self.sellbutton_handler)
        self.receiveButton.clicked.connect(self.receivebutton_handler)

    def sellbutton_handler(self):
        self.open_sell.emit()
    
    def receivebutton_handler(self):
        self.open_receive.emit()

class SellWindow(QtWidgets.QMainWindow, Ui_SellWindow):

    go_back = QtCore.pyqtSignal()
    sell_txn = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.homeButton.clicked.connect(self.homebutton_handler)
        self.sellConfirmButton.clicked.connect(self.sellbutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()
    
    def sellbutton_handler(self):
        self.sell_txn.emit()

class ReceiveWindow(QtWidgets.QMainWindow, Ui_ReceiveWindow):

    go_back = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.homeButton.clicked.connect(self.homebutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()


class Controller:

    currentWindow = None

    def __init__(self, rpcclient):
        self.client = rpcclient

    def show_main(self):
        self.mainwindow = MainWindow()
        self.mainwindow.open_sell.connect(self.show_sell)
        self.mainwindow.open_receive.connect(self.show_receive)
        self.mainwindow.show()
        if (self.currentWindow):
            self.currentWindow.close()

    def show_sell(self):
        self.sell = SellWindow()
        self.sell.go_back.connect(self.show_main)
        self.sell.sell_txn.connect(self.sell_txn)
        self.sell.show()
        self.mainwindow.hide()
        self.currentWindow = self.sell
    
    def show_receive(self):
        self.receive = ReceiveWindow()
        self.receive.go_back.connect(self.show_main)
        self.receive.show()
        self.mainwindow.hide()
        self.currentWindow = self.receive
        self.list_receive()
    
    def sell_txn(self):
        products = {
            1: "Drug 1",
            2: "Drug 2"
        }
        pName = products[self.sell.productName.currentIndex()]
        quantity = self.sell.quantity.value()
        buyerID = self.sell.buyerID.text()
        print(pName, quantity, buyerID)

        # Generate JSON data
        jsonData = { "json" : {
            "sellerID": "tut01",
            "buyerID": buyerID,
            "productID": "__BARCODE_HERE__",
            "productName": pName,
            "quantity": quantity
        }}
        self.client.makeSellTxn(jsonData)
    
    def list_receive(self):
        streamName = "tutstream"
        buyerId = "dist123"
        itemString = self.client.getStreamItems(streamName, buyerId)
        self.receive.itemList.setReadOnly(True)
        self.receive.itemList.setPlainText(itemString)


def main():
    rpcport = "7077"
    rootNode = "CounterChain@13.233.74.156:7445"
    rpcpassword = MCNodeCreator().startMCNode(rpcport, rootNode)
    rpcclient = MCClient("localhost", rpcport, "multichainrpc", rpcpassword)

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller(rpcclient)
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()