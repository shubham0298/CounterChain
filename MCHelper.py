import mcrpc
import os, subprocess, time

class MCClient(mcrpc.RpcClient):

    def __init__(self, host, port, user, pwd, use_ssl=False):
        super().__init__(host, port, user, pwd, use_ssl=use_ssl)

        # Get my address
        addressList = self.listaddresses()
        for address in addressList:
            if (address['ismine']):
                self.address = address['address']
                break

        print("My address:",self.address)

        # Subscribe to tutorial stream
        self.itemStream = "Istream"
        self.publisherStream = "Pstream"
        self.subscribe(self.itemStream)
        self.subscribe(self.publisherStream)
    
    def publishTxn(self, jsonData):
        # Publish data to tutorial stream
        clientKey = "clientKey"
        self.publish(self.itemStream, clientKey, jsonData)
    
    def addressOfTxnId(self, txnId):
        for item in self.liststreamitems(self.publisherStream):
            jsonData = item["data"]["json"]
            if (jsonData["Txnid"] == txnId):
                return jsonData["Publisher"]
        return None
    
    def receivableItems(self, sellerId, buyerId):
        sellerPubAddr = self.addressOfTxnId(sellerId)
        itemList = []
        if sellerPubAddr:
            for item in self.liststreampublisheritems(self.itemStream, sellerPubAddr):
                jsonData = item["data"]["json"]
                if (jsonData["BuyerId"] == buyerId):
                    itemList.append(jsonData)
        return itemList

class Query:
    def __init__(self, client, sellerid):
        self.comlist = client.getstreamitems("Istream")
        self.idlist = client.getstreamitems("Pstream")
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

    def __init__(self):
        pass

    def startMCNode(self, port, rootNode):
        cwd = os.getcwd()
        print(cwd)

        datadir = cwd + "\\chains"
        print(datadir)
        print(os.path.isdir(datadir))
        bindir = cwd + "\\bin"
        print(bindir)
        print(os.path.isdir(bindir))

        # port = "7077"
        # rootNode = "CounterChain@13.233.74.156:7445"

        os.chdir(bindir)
        print(os.getcwd())
        print("Starting MultiChain Node...")
        proc = subprocess.Popen(["multichaind", "-datadir="+datadir, "-rpcport="+port, rootNode], stdout=subprocess.PIPE, text=True)
        # proc = subprocess.Popen(["multichaind", "-rpcport="+port, rootNode], stdout=subprocess.PIPE, text=True)
        os.chdir(cwd)
        try:
            outs, errs = proc.communicate(timeout=5)
            # Permissions not granted i.e not yet registered
            outs = outs.split()
            walletAddress = outs[outs.index("multichain-cli") + 3]
            return walletAddress
        except subprocess.TimeoutExpired:
            # Node initialised successfully, now connect to rpcport
            # Get password
            print("Obtain rpcpassword")
            configFile = datadir + "\\CounterChain\\multichain.conf"
            conf = open(configFile, 'r')
            conf.readline()
            line = conf.readline().strip().split("=")
            rpcpassword = line[1]
            conf.close()
            # print(rpcpassword)
            return rpcpassword
        
        
        # time.sleep(5)
        # subprocess.run(["multichaind"])