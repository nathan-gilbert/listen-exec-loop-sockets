from ThreadedServer import ThreadedServer

class ListenLooper(ThreadedServer):
    def __init__(self, host, port):
        ThreadedServer.__init__(self, host, port)

if __name__ == "__main__":
    ListenLooper('localhost', 5432).listen()
