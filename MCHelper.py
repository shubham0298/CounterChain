import mcrpc
import os, subprocess, time
import hashlib

class MCClient(mcrpc.RpcClient):

    GOOD = 0
    SUBSCRIBE_ERROR = 1
    PUBLISH_ERROR = 2
    STREAM_ERROR = 3

    def __init__(self, host, port, user, pwd, use_ssl=False):
        super().__init__(host, port, user, pwd, use_ssl=use_ssl)
        self.status = None

        # Get my address
        try:
            addressList = self.listaddresses()
            for address in addressList:
                if (address['ismine']):
                    self.address = address['address']
                    break
            print("My address:",self.address)
        except Exception as e:
            print(e)
            return

        # Subscribe to tutorial stream
        self.itemStream = "Istream"
        self.publisherStream = "Pstream"
        try:
            self.subscribe(self.itemStream)
            self.subscribe(self.publisherStream)
        except Exception as e:
            print(e)
            self.status = self.SUBSCRIBE_ERROR
            return
        self.status = self.GOOD
        self.key = hashlib.sha1(bytes(pwd, "utf-8")).hexdigest()
    
    def publishTxn(self, jsonData):
        # Publish data to tutorial stream
        try:
            self.status = self.GOOD
            self.publish(self.itemStream, self.key, jsonData)
        except Exception as e:
            print(e)
            self.status = self.PUBLISH_ERROR
    
    # def addressOfTxnId(self, txnId):
    #     for item in self.liststreamitems(self.publisherStream):
    #         jsonData = item["data"]["json"]
    #         if (jsonData["Txnid"] == txnId):
    #             return jsonData["Publisher"]
    #     return None
    
    def userExists(self, txnId):
        try:
            self.status = self.GOOD
            for item in self.liststreamitems(self.publisherStream):
                jsonData = item["data"]["json"]
                if (jsonData["Txnid"] == txnId):
                    return True
            return False
        except Exception as e:
            print(e)
            self.status = self.STREAM_ERROR
            return None
    
    def receivableItems(self, buyerId):
        itemList = []
        receivedList = self.receivedItems(buyerId)
        
        if (receivedList is None):
            return None

        try:
            self.status = self.GOOD
            for item in self.liststreamitems(self.itemStream):
                jsonData = item["data"]["json"]
                print(jsonData)
                if (jsonData["BuyerId"] == buyerId and jsonData["Status"] == "PENDING" and jsonData["PId"] not in receivedList):
                    itemList.append(jsonData)
            return itemList
        except Exception as e:
            print(e)
            self.status = self.STREAM_ERROR
            return None
    
    def receivedItems(self, buyerId):
        itemList = []
        try:
            self.status = self.GOOD
            for item in self.liststreampublisheritems(self.itemStream, self.address):
                jsonData = item["data"]["json"]
                print(jsonData)
                if (jsonData["BuyerId"] == buyerId):
                    itemList.append(jsonData["PId"])
            return itemList
        except Exception as e:
            print(e)
            self.status = self.STREAM_ERROR
            return None

class Query:
    def __init__(self, client):
        self.comlist = client.liststreamitems("Istream")
        self.idlist = client.liststreamitems("Pstream")
    
    def init(self, sellerid):
        self.i = len(self.comlist) - 1
        self.response = "Authentic"
        self.owner = sellerid

    def check(self,p):
        flag = 0
        #first iteration
        for x in self.comlist[::-1]:
        #print(x)
            self.i=self.i-1
            l=x["data"]
        #print(l)
            if l['json']['PId']==p and l['json']['Status']=='COMPLETE' :
                flag=1
                print("Current Owner:",l['json']['BuyerId'])
                if l['json']['BuyerId']==self.owner:
                    #print(self.i)
                    self.checkloop(l['json']['SellerId'],p)
                    break
                else:
                    #print("Counterfeit drug!")
                    self.response="Counterfeit"
        if flag==0:
            #print("Counterfeit drug!")
            self.response="Counterfeit"


    def checkloop(self,m,p):
        flag = 0
        #map seller id to publisher id
        for y in self.idlist:
            users=y["data"]
            if(users['json']['Txnid']==m):
                pub=users['json']['Publisher']
                #print(pub)
        if self.i<0:
            print("Done")
        while(self.i>=0):
            #print(self.i)
            #p is string and change Buyer id
            if(self.comlist[self.i]['publishers'][0]==pub and self.comlist[self.i]['data']['json']['PId']==p and self.comlist[self.i]['data']['json']['Status']=='COMPLETE'):
                print("Found Another")
                if self.comlist[self.i]['data']['json']['BuyerId']==m:
                    flag=1
                    print("Previous Owner:",self.comlist[self.i]['data']['json']['BuyerId'])
                    self.i -= 1
                    self.checkloop(self.comlist[self.i+1]['data']['json']['SellerId'],p)
                    break
            self.i=self.i-1
        if flag==0 and self.i>=0:
            #print("Counterfeit drug!")
            self.response="Counterfeit"

class MCNodeCreator:
    
    HAS_PASSWORD = 1
    HAS_WALLET_ADDRESS = 2

    def __init__(self):
        self.root = os.getcwd()
        self.datadir = self.root + "\\chains"
        self.bindir = self.root + "\\bin"
        self.configFile = self.datadir + "\\CounterChain\\multichain.conf"
        self.status = None
        self.walletAddress = None
        self.rpcpassword = None
        self.proc = None

    def initPath(self):
        os.chdir(self.root)

    def initMCNode(self, localRpcPort, rootNode):
        # port = "7077"
        # rootNode = "CounterChain@counterchain.ddns.net:7445"
        self.initPath()
        os.chdir(self.bindir)

        self.proc = subprocess.Popen(["multichaind", "-datadir="+self.datadir, "-rpcport="+localRpcPort, rootNode], stdout=subprocess.PIPE, text=True)
        # self.proc = subprocess.Popen(["multichaind", "-rpcport="+port, rootNode], stdout=subprocess.PIPE, text=True)
        try:
            outs, errs = self.proc.communicate(timeout=5)
            # Permissions not granted i.e not yet registered
            outs = outs.split()
            self.walletAddress = outs[outs.index("multichain-cli") + 3]
            self.status = self.HAS_WALLET_ADDRESS
        except subprocess.TimeoutExpired:
            self.proc.kill()
            self.status = None

    def startMCNode(self, localRpcPort, rootNode):
        # port = "7077"
        # rootNode = "CounterChain@counterchain.ddns.net:7445"

        self.initPath()
        os.chdir(self.bindir)
        print("Starting MultiChain Node...")
        self.proc = subprocess.Popen(["multichaind", "-datadir="+self.datadir, "-rpcport="+localRpcPort, rootNode], stdout=subprocess.PIPE, text=True)
        # self.proc = subprocess.Popen(["multichaind", "-rpcport="+port, rootNode], stdout=subprocess.PIPE, text=True)
        time.sleep(5)
        try:
            # Node initialised successfully, now get password
            print("Obtain rpcpassword")
            conf = open(self.configFile, 'r')
            conf.readline()
            line = conf.readline().strip().split("=")
            self.rpcpassword = line[1]
            self.status = self.HAS_PASSWORD
            conf.close()
        except Exception as e:
            print(e)
            self.proc.kill()
            self.status = None
    
    def stopMCNode(self):
        self.proc.kill()