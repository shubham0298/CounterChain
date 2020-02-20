import sys
from MCHelper import MCClient, MCNodeCreator
from SocketHelper import SocketHelper
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_DashboardWindow
from ui_sell import Ui_SellWindow
from ui_receive import Ui_ReceiveWindow
from ui_inventory import Ui_inventory
from ui_itemadd import Ui_itemadd
from ui_login import Ui_loginWindow
from ui_register import Ui_registerWindow

class LoginWindow(QtWidgets.QMainWindow, Ui_loginWindow):

    open_dash = QtCore.pyqtSignal()
    open_reg = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.login.clicked.connect(self.loginbutton_handler)
        self.register_2.clicked.connect(self.regbutton_handler)

    def loginbutton_handler(self):
        self.open_dash.emit()

    def regbutton_handler(self):
        self.open_reg.emit()

class RegWindow(QtWidgets.QMainWindow, Ui_registerWindow):

    go_back = QtCore.pyqtSignal()
    init_reg = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.backButton.clicked.connect(self.homebutton_handler)
        self.submitButton.clicked.connect(self.registerbutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()
    
    def registerbutton_handler(self):
        self.init_reg.emit()

class DashWindow(QtWidgets.QMainWindow, Ui_DashboardWindow):

    open_sell = QtCore.pyqtSignal()
    open_receive = QtCore.pyqtSignal()
    open_additem = QtCore.pyqtSignal()
    open_inventory = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.sellButton.clicked.connect(self.sellbutton_handler)
        self.receiveButton.clicked.connect(self.receivebutton_handler)
        self.addButton.clicked.connect(self.addbutton_handler)
        self.inventoryButton.clicked.connect(self.inventbutton_handler)

    def sellbutton_handler(self):
        self.open_sell.emit()
    
    def receivebutton_handler(self):
        self.open_receive.emit()
    
    def addbutton_handler(self):
        self.open_additem.emit()

    def inventbutton_handler(self):
        self.open_inventory.emit()

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

class AddWindow(QtWidgets.QMainWindow, Ui_itemadd):

    go_back = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.back.clicked.connect(self.homebutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()

class InventoryWindow(QtWidgets.QMainWindow, Ui_inventory):

    go_back = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.homebutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()

class Controller:

    currentWindow = None

    def __init__(self):
        self.client = None
        self.userid = None
        self.role = None
        self.socket = SocketHelper()
    
    def show_login(self):
        self.loginwindow = LoginWindow()
        self.loginwindow.open_dash.connect(self.initiate_login)
        self.loginwindow.open_reg.connect(self.show_reg)
        self.loginwindow.show()
        if (self.currentWindow):
            self.currentWindow.close()
        self.currentWindow = self.loginwindow

    def show_reg(self):
        self.regwindow = RegWindow()
        self.regwindow.go_back.connect(self.show_login)
        self.regwindow.init_reg.connect(self.initiate_registration)
        self.regwindow.show()
        self.loginwindow.hide()
        self.currentWindow = self.regwindow

    def show_main(self):
        self.mainwindow = DashWindow()
        self.mainwindow.open_sell.connect(self.show_sell)
        self.mainwindow.open_receive.connect(self.show_receive)
        self.mainwindow.open_additem.connect(self.show_additem)
        self.mainwindow.open_inventory.connect(self.show_inventory)
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

    def show_additem(self):
        self.additem = AddWindow()
        self.additem.go_back.connect(self.show_main)
        self.additem.show()
        self.mainwindow.hide()
        self.currentWindow = self.additem

    def show_inventory(self):
        self.invent = InventoryWindow()
        self.invent.go_back.connect(self.show_main)
        self.invent.show()
        self.mainwindow.hide()
        self.currentWindow = self.invent
    
    def show_receive(self):
        self.receive = ReceiveWindow()
        self.receive.go_back.connect(self.show_main)
        self.receive.show()
        self.mainwindow.hide()
        self.currentWindow = self.receive
        self.list_receive()
    
    def initiate_login(self):
        # socket code here
        login_data = [self.loginwindow.id_lineEdit.text(), self.loginwindow.paswd_lineEdit.text()]
        result = self.socket.login(login_data)
        # returns result object
        # result = {
        #     "success": True,
        #     "status": "ACCEPT/PENDING/REJECT", or Error msg
        #     "userid": txn_id,
        #     "role": role
        # }
        
        if (result["success"] == True and result["status"] == "ACCEPT"):
            rpcport = "7077"
            rootNode = "CounterChain@35.154.49.40:7445"
            rpcpassword = MCNodeCreator().startMCNode(rpcport, rootNode)
            self.client = MCClient("localhost", rpcport, "multichainrpc", rpcpassword)

            self.userid = result["userid"]
            self.role = result["role"]
            self.show_main()
        elif (result["success"] == True and result["status"] == "PENDING"):
            print("Verification under process")
        else:
            print("{}:Login failed".format(result["status"]))
    
    def initiate_registration(self):
        # socket code here
        # upload details and files
        # upload node wallet address
        rpcport = "7077"
        rootIP = self.socket.resolve("counterchain.ddns.net")
        rootNode = "CounterChain@" + rootIP + ":7445"
        walletAddress = MCNodeCreator().startMCNode(rpcport, rootNode)
        roles = {
            0: "Manufacturer",
            1: "Distributor",
            2: "Retailer"
        }
        newUserData = []
        newUserData.append(self.regwindow.paswd_LE.text())
        newUserData.append(self.regwindow.name_LE.text())
        newUserData.append(roles[self.regwindow.role.currentIndex()])
        newUserData.append(walletAddress)
        newUserData.append(self.regwindow.email_LE.text())
        newUserData.append(self.regwindow.phone_LE.text())

        result = self.socket.register(newUserData)
        # returns result object
        # result = {
        #     "success": True,
        #     "status": "PENDING", or Error msg
        #     "userID": txn_id
        # }

        if (result["success"] == True):
            print("Registration success. Verification under process for address:", walletAddress)
            print("Your user id:", result["userid"])
            self.show_login()
        else:
            print("{}:Registration failed".format(result["status"]))
    
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
            "sellerID": self.userid,
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
    # rpcport = "7077"
    # rootNode = "CounterChain@35.154.49.40:7445"
    # rpcpassword = MCNodeCreator().startMCNode(rpcport, rootNode)
    # rpcclient = MCClient("localhost", rpcport, "multichainrpc", rpcpassword)

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()