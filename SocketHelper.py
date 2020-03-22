import socket

class SocketHelper:

    SOCKET_ERROR = 1
    LOGIN_FAIL = 2
    REGISTER_FAIL = 3

    def __init__(self):
        socket.setdefaulttimeout(4)

    def resolve(self, url):
        try:
            return socket.gethostbyname(url)
        except OSError:
            return self.SOCKET_ERROR
    
    def login(self, data):
        result = {"success": None, "status": None, "userid": None, "role": None}
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except OSError:
            result["success"] = False
            result["status"] = self.SOCKET_ERROR
        try:
            s.connect(("counterchain.ddns.net", 7123))
            s.sendall(bytes("LOGIN:{}:{}\n".format(data[0], data[1]), "utf-8"))
            response = str(s.recv(1024), "utf-8").strip()
            response = response.split()
            print(response)
            if (response[0] == "SUCCESS"):
                result["success"] = True
                result["status"] = response[1]
                result["userid"] = data[0]
                result["role"] = response[2]
            else:
                result["success"] = False
                result["status"] = self.LOGIN_FAIL
            s.close()
        except OSError:
            s.close()
            result["success"] = False
            result["status"] = self.SOCKET_ERROR
        return result
    
    def register(self, data):
        result = {"success": None, "status": None, "userid": None}
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except OSError:
            result["success"] = False
            result["status"] = self.SOCKET_ERROR
        try:
            s.connect(("counterchain.ddns.net", 7123))
            dataStr = ":".join(data)
            print("Sending:", dataStr)
            s.sendall(bytes("REGISTER:{}\n".format(dataStr), "utf-8"))
            response = str(s.recv(1024), "utf-8").strip()
            response = response.split()
            print(response)
            if (response[0] == "SUCCESS"):
                result["success"] = True
                result["status"] = response[0]
                result["userid"] = response[1]
            else:
                result["success"] = False
                result["status"] = self.REGISTER_FAIL
            s.close()
        except OSError:
            s.close()
            result["success"] = False
            result["status"] = self.SOCKET_ERROR
        return result