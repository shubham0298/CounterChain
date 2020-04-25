import sys, re, sqlite3
from MCHelper import MCClient, MCNodeCreator, Query
from SocketHelper import SocketHelper
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_DashboardWindow
from ui_sell import Ui_SellWindow
from ui_receive import Ui_ReceiveWindow
from ui_inventory import Ui_inventory
from ui_itemadd import Ui_itemadd
from ui_login import Ui_loginWindow
from ui_aboutus import Ui_aboutus
from ui_register import Ui_registerWindow
from ui_dashboardother import Ui_DashboardWindow_other

class LoginWindow(QtWidgets.QMainWindow, Ui_loginWindow):

    open_dash = QtCore.pyqtSignal()
    open_reg = QtCore.pyqtSignal()
    open_aboutus = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.login.clicked.connect(self.loginbutton_handler)
        self.aboutus.clicked.connect(self.aboutbutton_handler)
        self.register_2.clicked.connect(self.regbutton_handler)

    def loginbutton_handler(self):
        self.open_dash.emit()

    def regbutton_handler(self):
        self.open_reg.emit()
    
    def aboutbutton_handler(self):
        self.open_aboutus.emit()

class AboutUsWindow(QtWidgets.QMainWindow, Ui_aboutus):

    close_about = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.backButton.clicked.connect(self.homebutton_handler)

    def homebutton_handler(self):
        self.close_about.emit()

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

        # Auto-completer drop down suggestions
        conn = sqlite3.connect('drug_stock.db')
        c = conn.cursor()
        c.execute("SELECT pid FROM stocks")
        lst = []
        for row in c.fetchall():
	        lst.append(row[0])
        conn.close()
        completer = QtWidgets.QCompleter(lst)
        self.pidLE.setCompleter(completer)

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

        self.tableWidget.setHorizontalHeaderLabels(["Product ID", "Product Name", "Quantity", "Status"])
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
        self.nodeCreator = MCNodeCreator()
    
    '''
        Window controllers
    '''
    def show_login(self):
        self.loginwindow = LoginWindow()
        self.loginwindow.open_dash.connect(self.initiate_login)
        self.loginwindow.open_reg.connect(self.show_reg)
        self.loginwindow.open_aboutus.connect(self.show_aboutus)
        self.loginwindow.show()
        if (self.currentWindow):
            self.currentWindow.close()
        self.currentWindow = self.loginwindow

    def show_aboutus(self):
        self.aboutwindow = AboutUsWindow()
        self.aboutwindow.close_about.connect(self.show_login)
        self.aboutwindow.show()
        self.currentWindow = self.aboutwindow

    def show_reg(self):
        self.regwindow = RegWindow()
        self.regwindow.go_back.connect(self.show_login)
        self.regwindow.init_reg.connect(self.validate_registration)
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
        self.mainwindow.role.setText("Role: " + self.role)
        self.mainwindow.uid.setText("Login ID: " + self.userid)
        if (self.currentWindow):
            self.currentWindow.close()
        self.stock_init()

    def show_sell(self):
        self.sell = SellWindow()
        self.sell.go_back.connect(self.show_main)
        self.sell.sell_txn.connect(self.validate_sell_txn)
        self.sell.clear_pid.connect(self.sell_clear)
        self.sell.reset_input.connect(self.sell_reset)
        self.sell.show()
        self.mainwindow.hide()
        self.currentWindow = self.sell

    def show_additem(self):
        self.additem = AddWindow()
        self.additem.go_back.connect(self.show_main)
        self.additem.add_product.connect(self.validate_add_txn)
        self.additem.show()
        self.mainwindow.hide()
        self.currentWindow = self.additem

    def show_inventory(self):
        self.invent = InventoryWindow()
        self.invent.go_back.connect(self.show_main)
        self.invent.show()
        self.mainwindow.hide()
        self.currentWindow = self.invent
        self.stock_list()
    
    def show_receive(self):
        self.receive = ReceiveWindow()
        self.receive.go_back.connect(self.show_main)
        self.receive.list_item.connect(self.rcv_list)
        self.receive.rcv_item.connect(self.rcv_txn)
        self.receive.rcv_all.connect(self.rcv_all)
        self.receive.show()
        self.mainwindow.hide()
        self.currentWindow = self.receive
        self.rcv_list()
    
    '''
        Login and Registration functions
    '''
    def initiate_login(self):
        login_data = [self.loginwindow.id_lineEdit.text().strip(), self.loginwindow.paswd_lineEdit.text().strip()]
        result = self.socket.login(login_data)
        # returns result object
        # result = {
        #     "success": True,
        #     "status": "ACCEPT/PENDING/REJECT", or Error msg
        #     "userid": txn_id,
        #     "role": role
        # }
        if (result["success"] == True and result["status"] == "ACCEPT"):
            self.loginwindow.statusLabel.setText("")

            rpcport = "7077"
            rootIP = self.socket.resolve("counterchain.ddns.net")
            rootNode = "CounterChain@" + rootIP + ":7445"
            self.nodeCreator.startMCNode(rpcport, rootNode)
            if (self.nodeCreator.status is None):
                self.show_dialog("Unable to start MultiChain process")
                return
            
            if (self.nodeCreator.status == MCNodeCreator.HAS_PASSWORD):
                self.client = MCClient("localhost", rpcport, "multichainrpc", self.nodeCreator.rpcpassword)

            if (self.client.status == MCClient.GOOD):
                self.userid = result["userid"]
                self.role = result["role"]
                self.show_main()
            else:
                self.show_dialog("Unable to connect to MultiChain RPC-Server")
        elif (result["success"] == True and result["status"] == "PENDING"):
            self.show_dialog("Verification for your account is under process.")
            print("Verification under process")
        elif (result["success"] == False and result["status"] == SocketHelper.LOGIN_FAIL):
            self.show_dialog("Incorrect username or password")
            print("{}:Login failed".format(result["status"]))
        elif (result["success"] == False and result["status"] == SocketHelper.SOCKET_ERROR):
            self.show_dialog("Connection to CounterChain server failed.\n\nPlease check your network connection.")
    
    def validate_registration(self):
        proper = True
        email_re = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        phone_re = r"([0-9]{10,10}$)"
        emailText = self.regwindow.email_LE.text().strip()
        nameText = self.regwindow.name_LE.text().strip()
        paswdText = self.regwindow.paswd_LE.text().strip()
        phoneText = self.regwindow.phone_LE.text().strip()
        licText = self.regwindow.lic_LE.text().strip()
        roleIndex = self.regwindow.role.currentIndex()

        if (emailText == ""):
            self.show_dialog("Enter E-mail ID")
            proper = False
        elif not (re.match(email_re, emailText)):
            self.show_dialog("Invalid E-mail")
            proper = False
        elif (len(paswdText) < 6):
            self.show_dialog("Enter password of at least 6 characters")
            proper = False
        elif (nameText == ""):
            self.show_dialog("Enter name")
            proper = False
        elif not (re.match(phone_re, phoneText)):
            self.show_dialog("Invalid Phone no.")
            proper = False
        elif (roleIndex == 0):
            self.show_dialog("Select Role")
            proper = False
        elif (licText == ""):
            self.show_dialog("Enter License number")
            proper = False
        
        if (proper):
            roles = {
            1: "Manufacturer",
            2: "Distributer",
            3: "Retailer"
            }
            newUserData = []
            newUserData.append(paswdText)
            newUserData.append(nameText)
            newUserData.append(roles[roleIndex])
            newUserData.append(emailText)
            newUserData.append(phoneText)
            newUserData.append(licText)
            self.initiate_registration(newUserData)

    def initiate_registration(self, newUserData):
        rpcport = "7077"
        rootIP = self.socket.resolve("counterchain.ddns.net")
        if (rootIP == SocketHelper.SOCKET_ERROR):
            self.show_dialog("Connection to CounterChain server failed.\n\nPlease check your network connection.")
            return
        
        rootNode = "CounterChain@" + rootIP + ":7445"
        self.nodeCreator.initMCNode(rpcport, rootNode)
        if (self.nodeCreator.status is None):
            self.show_dialog("Unable to initiate MultiChain Node.")
            return
        
        if (self.nodeCreator.status == MCNodeCreator.HAS_WALLET_ADDRESS):
            newUserData.insert(3, self.nodeCreator.walletAddress)
            result = self.socket.register(newUserData)
            # returns result object
            # result = {
            #     "success": True,
            #     "status": "PENDING", or Error msg
            #     "userID": txn_id
            # }
            if (result["success"] == True):
                self.show_dialog("Registration is successful.\n\nYour Login ID is {}\n\nPlease note it down for further use.".format(result["userid"]))
                print("Registration success. Verification under process for address:", self.nodeCreator.walletAddress)
                print("Your user id:", result["userid"])
                self.show_login()
            elif (result["status"] == SocketHelper.REGISTER_FAIL):
                self.show_dialog("Registration failed as ID already exists.")
                print("{}:Registration failed".format(result["status"]))
            elif (result["status"] == SocketHelper.SOCKET_ERROR):
                self.show_dialog("Connection to CounterChain server failed.\n\nPlease check your network connection.")

    '''
        Add window functions
    '''
    def validate_add_txn(self):
        proper = True
        pidText = self.additem.pidLE.text().strip()
        pnameText = self.additem.pnameLE.text().strip()

        if (len(pidText) == 0):
            self.show_dialog("Enter Product ID")
            proper = False
        elif (len(pnameText) == 0):
            self.show_dialog("Enter Product Name")
            proper = False
        
        if proper:
            self.add_txn([pidText, pnameText])
    
    def add_txn(self, productData):
        conn = sqlite3.connect('drug_stock.db')
        c = conn.cursor()
        # c.execute("CREATE TABLE if not exists stocks(pid TEXT PRIMARY KEY, pname TEXT, quantity INTEGER, status TEXT)")
        try:
            # Generate JSON data
            jsonData = { "json": {
                "PId": productData[0],
                "PName": productData[1],
                "SellerId": self.userid,
                "BuyerId": self.userid,
                "Status": "COMPLETE"
            }}
            self.client.publishTxn(jsonData)
            if (self.client.status == MCClient.PUBLISH_ERROR):
                self.show_dialog("Unable to add product")
            else:
                c.execute("INSERT INTO stocks VALUES(?,?,?,?)", (productData[0], productData[1], 1, "In Stock"))
                self.show_dialog("Product Registered!")
        except:
            self.show_dialog("Product ID Exists!")
            print("ID Already Exist!")
        finally:
            conn.commit()
            conn.close()

    '''
        Sell window functions
    '''
    def validate_sell_txn(self):
        proper = True
        pidText = self.sell.pidLE.text().strip()
        buyeridText = self.sell.buyeridLE.text().strip()

        if (len(pidText) == 0):
            self.show_dialog("Enter Product ID")
            proper = False
        elif (len(buyeridText) == 0):
            self.show_dialog("Enter Buyer ID")
            proper = False
        elif (buyeridText == self.userid):
            self.show_dialog("Cannot sell to self")
            proper = False
        elif (not self.client.userExists(buyeridText) and self.client.status == MCClient.GOOD):
            self.show_dialog("No such buyer exists")
            proper = False
        elif (self.client.status == MCClient.STREAM_ERROR):
            self.show_dialog("Unable to fetch buyer list")
            proper = False
        
        if proper:
            self.sell_txn([pidText, buyeridText])
    
    def sell_txn(self, sellData):
        conn = sqlite3.connect('drug_stock.db')
        c = conn.cursor()
        
        c.execute('''SELECT status,pname FROM stocks WHERE pid=?''', (sellData[0],))
        pdata = c.fetchone()
        if (pdata == None):
            self.show_dialog("No such product")
        elif (pdata[0] == "Sold Out"):
            self.show_dialog("Product(s) out of Stock!")
        else:
            # Generate JSON data
            jsonData = { "json" : {
                "PId": sellData[0],
                "PName": pdata[1],
                "SellerId": self.userid,
                "BuyerId": sellData[1],
                "Status": "PENDING"
            }}
            self.client.publishTxn(jsonData)
            if (self.client.status == MCClient.PUBLISH_ERROR):
                self.show_dialog("Unable to sell product")
            else:
                c.execute('''UPDATE stocks SET status="Sold Out" WHERE pid=?''', (sellData[0],))
                self.show_dialog("Product(s) Sold")
                conn.commit()
        conn.close()
    
    def sell_clear(self):
        self.sell.pidLE.clear()
    
    def sell_reset(self):
        self.sell.pidLE.clear()
        self.sell.buyeridLE.clear()
    
    '''
        Receive window functions
    '''
    def rcv_list(self):
        # sellerId = self.receive.selleridLE.text()
        buyerId = self.userid
        itemList = self.client.receivableItems(buyerId)
        if (self.client.status != MCClient.GOOD):
            self.show_dialog("Unable to fetch transaction list")
            return
        queryProcess = Query(self.client)

        self.receive.rcvTable.clear()
        self.receive.rcvTable.setRowCount(0)
        for row,items in enumerate(itemList):
            self.receive.rcvTable.insertRow(row)
            self.receive.rcvTable.setItem(row, 0, QtWidgets.QTableWidgetItem(items["SellerId"]))
            self.receive.rcvTable.setItem(row, 1, QtWidgets.QTableWidgetItem(items["PId"]))
            self.receive.rcvTable.setItem(row, 2, QtWidgets.QTableWidgetItem(items["PName"]))
            queryProcess.init(items["SellerId"])
            queryProcess.check(items["PId"])
            self.receive.rcvTable.setItem(row, 3, QtWidgets.QTableWidgetItem(queryProcess.response))
        
        self.receive.rcvTable.setHorizontalHeaderLabels(["Seller ID", "Product ID", "Product Name", "Status"])
        self.receive.rcvTable.resizeColumnsToContents()
        self.receive.rcvTable.resizeRowsToContents()
    
    def rcv_txn(self):
        selectedItem = self.receive.rcvTable.currentItem()
        row =  self.receive.rcvTable.row(selectedItem)

        if (selectedItem and self.receive.rcvTable.item(row, 3).text() == "Authentic"):
            # Generate JSON data
            jsonData = { "json" : {
                "PId": self.receive.rcvTable.item(row, 1).text(),
                "PName": self.receive.rcvTable.item(row, 2).text(),
                "SellerId": self.receive.rcvTable.item(row, 0).text(),
                "BuyerId": self.userid,
                "Status": "COMPLETE"
            }}
            self.client.publishTxn(jsonData)
            if (self.client.status == MCClient.GOOD):
                self.receive.rcvTable.removeRow(row)
                self.add_to_stock(jsonData["json"]["PId"], jsonData["json"]["PName"])
            else:
                self.show_dialog("Unable to receive product")
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
                if (self.client.status == MCClient.GOOD):
                    self.receive.rcvTable.removeRow(row)
                    self.add_to_stock(jsonData["json"]["PId"], jsonData["json"]["PName"])
                else:
                    self.show_dialog("Unable to receive product")
            else:
                row += 1
            rowCount = self.receive.rcvTable.rowCount()
    
    '''
        drug_stock database handlers
    '''
    def stock_init(self):
        conn = sqlite3.connect('drug_stock.db')
        c = conn.cursor()
        c.execute("CREATE TABLE if not exists stocks(pid TEXT PRIMARY KEY, pname TEXT, quantity INTEGER, status TEXT)")
        conn.commit()
        conn.close()
    
    def stock_list(self):
        conn = sqlite3.connect('drug_stock.db')
        try:
            result = conn.execute("SELECT * FROM stocks")
            for row_no, row_data in enumerate(result):
                self.invent.tableWidget.setRowCount(row_no + 1)
                for col_no, col_data in enumerate(row_data):
                    self.invent.tableWidget.setItem(row_no, col_no, QtWidgets.QTableWidgetItem(str(col_data)))
        except:
            print("No Table Found!")
        conn.close()

    def add_to_stock(self, pid, pname):
        conn = sqlite3.connect('drug_stock.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO stocks VALUES(?,?,?,?)", (pid, pname, "1", "In Stock"))
            conn.commit()
            self.show_dialog("Product(s) Received")
        except:
            self.show_dialog("Product Already Exists!")
        conn.close()

    '''
        Miscellaneous functions
    '''
    def do_logout(self):
        if (self.mainwindow):
            self.mainwindow.close()
        self.client.stop()
        self.show_login()
    
    def show_dialog(self, txt):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("CounterChain")
        msg.setText(txt)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

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