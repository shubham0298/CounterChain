import sys
from MCHelper import MCClient, MCNodeCreator, Query
from SocketHelper import SocketHelper
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_DashboardWindow
from ui_sell import Ui_SellWindow
from ui_receive import Ui_ReceiveWindow
from ui_inventory import Ui_inventory
from ui_itemadd import Ui_itemadd
from ui_login import Ui_loginWindow
from ui_register import Ui_registerWindow
from ui_dashboardother import Ui_DashboardWindow_other

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
    logout_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.sellButton.clicked.connect(self.sellbutton_handler)
        self.receiveButton.clicked.connect(self.receivebutton_handler)
        self.addButton.clicked.connect(self.addbutton_handler)
        self.inventoryButton.clicked.connect(self.inventbutton_handler)
        self.logout.clicked.connect(self.logout_handler)

    def sellbutton_handler(self):
        self.open_sell.emit()
    
    def receivebutton_handler(self):
        self.open_receive.emit()
    
    def addbutton_handler(self):
        self.open_additem.emit()

    def inventbutton_handler(self):
        self.open_inventory.emit()

    def logout_handler(self):
        self.logout_signal.emit()

class DashWindowother(QtWidgets.QMainWindow, Ui_DashboardWindow_other):

    open_sell = QtCore.pyqtSignal()
    open_receive = QtCore.pyqtSignal()
    open_inventory = QtCore.pyqtSignal()
    logout_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.sellButton.clicked.connect(self.sellbutton_handler)
        self.receiveButton.clicked.connect(self.receivebutton_handler)
        self.inventoryButton.clicked.connect(self.inventbutton_handler)
        self.logout.clicked.connect(self.logout_handler)

    def sellbutton_handler(self):
        self.open_sell.emit()
    
    def receivebutton_handler(self):
        self.open_receive.emit()

    def inventbutton_handler(self):
        self.open_inventory.emit()

    def logout_handler(self):
        self.logout_signal.emit()

class SellWindow(QtWidgets.QMainWindow, Ui_SellWindow):

    go_back = QtCore.pyqtSignal()
    sell_txn = QtCore.pyqtSignal()
    reset_input = QtCore.pyqtSignal()
    clear_pid = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.homeButton.clicked.connect(self.homebutton_handler)
        self.sellConfirmButton.clicked.connect(self.sellbutton_handler)
        self.clearButton.clicked.connect(self.clearbutton_handler)
        self.resetButton.clicked.connect(self.resetbutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()
    
    def sellbutton_handler(self):
        self.sell_txn.emit()
    
    def resetbutton_handler(self):
        self.reset_input.emit()
    
    def clearbutton_handler(self):
        self.clear_pid.emit()

class ReceiveWindow(QtWidgets.QMainWindow, Ui_ReceiveWindow):

    go_back = QtCore.pyqtSignal()
    list_item = QtCore.pyqtSignal()
    rcv_item = QtCore.pyqtSignal()
    rcv_all = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.homeButton.clicked.connect(self.homebutton_handler)
        self.checkButton.clicked.connect(self.checkbutton_handler)
        self.rcvButton.clicked.connect(self.rcvbutton_handler)
        self.rcvallButton.clicked.connect(self.rcvallbutton_handler)

    def homebutton_handler(self):
        self.go_back.emit()
    
    def checkbutton_handler(self):
        self.list_item.emit()
    
    def rcvbutton_handler(self):
        self.rcv_item.emit()
    
    def rcvallbutton_handler(self):
        self.rcv_all.emit()

class AddWindow(QtWidgets.QMainWindow, Ui_itemadd):

    go_back = QtCore.pyqtSignal()
    add_product = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.back.clicked.connect(self.homebutton_handler)
        self.addButton.clicked.connect(self.addproduct_handler)

    def homebutton_handler(self):
        self.go_back.emit()
    
    def addproduct_handler(self):
        self.add_product.emit()

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
        if(self.role == "Manufacturer"):
            self.mainwindow = DashWindow()
            self.mainwindow.open_additem.connect(self.show_additem)
        else:
            self.mainwindow = DashWindowother()
        self.mainwindow.open_sell.connect(self.show_sell)
        self.mainwindow.open_receive.connect(self.show_receive)
        self.mainwindow.open_inventory.connect(self.show_inventory)
        self.mainwindow.logout_signal.connect(self.do_logout)
        self.mainwindow.show()
        self.mainwindow.role.setText("Role: "+self.role)
        self.mainwindow.uid.setText("Login ID: "+self.userid)
        if (self.currentWindow):
            self.currentWindow.close()

    def show_sell(self):
        self.sell = SellWindow()
        self.sell.go_back.connect(self.show_main)
        self.sell.sell_txn.connect(self.sell_txn)
        self.sell.clear_pid.connect(self.sell_clear)
        self.sell.reset_input.connect(self.sell_reset)
        self.sell.show()
        self.mainwindow.hide()
        self.currentWindow = self.sell

    def show_additem(self):
        self.additem = AddWindow()
        self.additem.go_back.connect(self.show_main)
        self.additem.add_product.connect(self.add_txn)
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
        self.receive.list_item.connect(self.rcv_list)
        self.receive.rcv_item.connect(self.rcv_txn)
        self.receive.rcv_all.connect(self.rcv_all)
        self.receive.show()
        self.mainwindow.hide()
        self.currentWindow = self.receive
        # self.list_receive()
    
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
            rootIP = self.socket.resolve("counterchain.ddns.net")
            rootNode = "CounterChain@" + rootIP + ":7445"
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
            1: "Distributer",
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
    
    def do_logout(self):
        if (self.mainwindow):
            self.mainwindow.close()
        self.show_login()
        self.client.stop()
    
    def add_txn(self):
        # Generate JSON data
        jsonData = { "json": {
            "PId": self.additem.pidLE.text(),
            "PName": self.additem.pnameLE.text(),
            "SellerId": self.userid,
            "BuyerId": self.userid,
            "Status": "COMPLETE"
        }}
        self.client.publishTxn(jsonData)

    def sell_txn(self):
        # Generate JSON data
        jsonData = { "json" : {
            "PId": self.sell.pidLE.text(),
            "PName": "dummy",
            "SellerId": self.userid,
            "BuyerId": self.sell.buyeridLE.text(),
            "Status": "PENDING"
        }}
        self.client.publishTxn(jsonData)
    
    def sell_clear(self):
        self.sell.pidLE.clear()
    
    def sell_reset(self):
        self.sell.pidLE.clear()
        self.sell.buyeridLE.clear()
    
    def rcv_list(self):
        sellerId = self.receive.selleridLE.text()
        buyerId = self.userid
        itemList = self.client.receivableItems(sellerId, buyerId)
        queryProcess = Query(self.client, sellerId)

        self.receive.rcvTable.clear()
        self.receive.rcvTable.setRowCount(0)
        for row,items in enumerate(itemList):
            self.receive.rcvTable.insertRow(row)
            self.receive.rcvTable.setItem(row, 0, QtWidgets.QTableWidgetItem(items["SellerId"]))
            self.receive.rcvTable.setItem(row, 1, QtWidgets.QTableWidgetItem(items["PId"]))
            self.receive.rcvTable.setItem(row, 2, QtWidgets.QTableWidgetItem(items["PName"]))
            queryProcess.check(items["PId"])
            self.receive.rcvTable.setItem(row, 3, QtWidgets.QTableWidgetItem(queryProcess.response))
        
        self.receive.rcvTable.setHorizontalHeaderLabels(["Seller ID", "Product ID", "Product Name", "Status"])
        self.receive.rcvTable.resizeColumnsToContents()
        self.receive.rcvTable.resizeRowsToContents()
    
    def rcv_txn(self):
        selectedItem = self.receive.rcvTable.currentItem()
        row =  self.receive.rcvTable.row(selectedItem)

        if (self.receive.rcvTable.item(row, 3).text() == "Authentic"):
            # Generate JSON data
            jsonData = { "json" : {
                "PId": self.receive.rcvTable.item(row, 1).text(),
                "PName": self.receive.rcvTable.item(row, 2).text(),
                "SellerId": self.receive.rcvTable.item(row, 0).text(),
                "BuyerId": self.userid,
                "Status": "COMPLETE"
            }}
            self.client.publishTxn(jsonData)
            self.receive.rcvTable.removeRow(row)
        else:
            print("Counterfeit")
    
    def rcv_all(self):
        rowCount = self.receive.rcvTable.rowCount()
        row = 0
        while (rowCount > 0 and row < rowCount):
            if (self.receive.rcvTable.item(row, 3).text() == "Authentic"):
                # Generate JSON data
                jsonData = { "json" : {
                    "PId": self.receive.rcvTable.item(row, 1).text(),
                    "PName": self.receive.rcvTable.item(row, 2).text(),
                    "SellerId": self.receive.rcvTable.item(row, 0).text(),
                    "BuyerId": self.userid,
                    "Status": "COMPLETE"
                }}
                self.client.publishTxn(jsonData)
                self.receive.rcvTable.removeRow(row)
            else:
                row += 1
            rowCount = self.receive.rcvTable.rowCount()

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