import socket

class SocketWorker:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def sendToListener(self):
        client, address = self.sock.accept()
        client.send(b"data")
        client.close()

if __name__ == "__main__":
    SocketWorker('localhost', 5433).sendToListener()
