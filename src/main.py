import socket
from src.settings import PORT

class TCPServer:
    def __init__(self):
        self._socket = socket.socket()

    def __enter__(self):
        host = socket.gethostname()
        self._socket.bind((host, PORT), )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def listen_for_requests(self):
        while True:
            self._socket.listen(2)
            connection, address = self._socket.accept()
            message = connection.recv(1024)
            print(message.decode())
            connection.send("Received".encode())
            connection.close()


class DatabaseInterface:
    def __init__(self):
        self._database = {}

    def set(self, key, value):
        self._database[key] = value

    def get(self, key):
        return self._database[key]

    def remove(self, key):
        self._database.pop(key)


def main():
    with TCPServer() as server:
        server.listen_for_requests()


if __name__ == "__main__":
    main()
