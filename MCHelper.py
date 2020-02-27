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
        self.streamName = "Itemstream"
        self.subscribe(self.streamName)
    
    def publishTxn(self, jsonData):
        # Publish data to tutorial stream
        clientKey = "clientKey"
        self.publish(self.streamName, clientKey, jsonData)
    
    def getStreamItems(self, buyerId):
        streamItems = self.liststreamitems(self.streamName)
        jsonData = []
        for items in streamItems:
            jsonData.append(items["data"]["json"])
        
        itemString = ""
        for txn in jsonData:
            key = txn.get('buyerID', "no key")
            if (key != "no key" and key == buyerId):
                itemString += txn["sellerID"] + "\t" + txn["productName"] + "\t" + str(txn["quantity"]) + "\n"
        
        return itemString

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