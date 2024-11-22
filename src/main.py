import socket
from src.settings import PORT


class TCPServer:
    def __init__(self):
        self._socket = socket.socket()
        self._database_wrapper = DatabaseWrapper()

    def __enter__(self):
        host = socket.gethostname()
        self._socket.bind((host, PORT), )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def listen_for_requests(self):
        while True:
            self._socket.listen(3)
            connection, address = self._socket.accept()
            message = connection.recv(1024).decode()
            print(f"Received message: {message}")

            return_message = self._database_wrapper.parse_message(message)

            connection.send(return_message.encode())
            connection.close()


class DatabaseWrapper:
    def __init__(self):
        self.database = DatabaseInterface()

    def parse_message(self, message):
        if len(message.split(" ")) > 3:
            raise Exception("Invalid query")
        if "GET" in message:
            command, key = message.split(" ")
            return self.run_get_query(key)
        elif "SET" in message:
            command, key, value = message.split(" ")
            return self.run_set_query(key, value)
        elif "DEL" in message:
            command, key = message.split(" ")
            return self.run_del_query(key)

    def run_get_query(self, key):
        return self.database.get(key)

    def run_set_query(self, key, value):
        return self.database.set(key, value)

    def run_del_query(self, key):
        return self.database.remove(key)


class DatabaseInterface:
    def __init__(self):
        self._database = {}

    def set(self, key, value):
        self._database[key] = value
        return "OK"

    def get(self, key):
        return self._database.get(key, "NULL")

    def remove(self, key):
        self._database.pop(key)
        return "Deleted"


def main():
    with TCPServer() as server:
        server.listen_for_requests()


if __name__ == "__main__":
    main()
