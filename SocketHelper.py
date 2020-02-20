import socket

class SocketHelper:
    def __init__(self):
        pass

    def resolve(self, url):
        return socket.gethostbyname(url)
    
    def login(self, data):
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the server
        s.connect(("counterchain.ddns.net", 7123))

        s.sendall(bytes("LOGIN:{}:{}\n".format(data[0], data[1]), "utf-8"))
        response = str(s.recv(1024), "utf-8").strip()
        response = response.split()
        print(response)
        result = {"success": None, "status": None, "userid": None, "role": None}
        if (response[0] == "SUCCESS"):
            result["success"] = True
            result["status"] = response[1]
            result["userid"] = data[0]
            result["role"] = response[2]
        else:
            result["success"] = False
            result["status"] = response[0]
        
        s.close()
        return result
    
    def register(self, data):
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the server
        s.connect(("counterchain.ddns.net", 7123))

        dataStr = ":".join(data)
        print("Sending:", dataStr)
        s.sendall(bytes("REGISTER:{}\n".format(dataStr), "utf-8"))
        response = str(s.recv(1024), "utf-8").strip()
        response = response.split()
        print(response)
        result = {"success": None, "status": None, "userid": None}
        if (response[0] == "SUCCESS"):
            result["success"] = True
            result["status"] = response[0]
            result["userid"] = response[1]
        else:
            result["success"] = False
            result["status"] = response[0]
        
        s.close()
        return result