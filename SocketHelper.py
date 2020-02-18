import socket

class SocketHelper:
    def __init__(self):
        pass

    def send(self, data):
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the server
        s.connect(("counterchain.ddns.net", 7123))

        s.sendall(bytes("{} {}\n".format(data[0], data[1]), "utf-8"))
        response = str(s.recv(1024), "utf-8")
        print(response)
        result = {"success": None, "status": None, "userid": None}
        if (response):
            result["success"] = True
            result["status"] = response.strip()
            result["userid"] = data[0]
        else:
            result["success"] = False
        
        return result