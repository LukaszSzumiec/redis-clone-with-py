import socket
import queue
import threading
import select
from src.settings import SERVER_ADDRESS, PORT, MAX_CLIENTS


class TCPServer:
    def __init__(self):
        self._socket = socket.socket()
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._database_wrapper = DatabaseWrapper()
        self.client_queue = queue.Queue()
        self.connections = [self._socket]
        self.clients = {}

    def __enter__(self):
        self._socket.bind(
            (SERVER_ADDRESS, PORT),
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def listen_for_requests(self):
        self._socket.listen(MAX_CLIENTS)
        while True:
            read_sockets, _, exception_sockets = select.select(
                self.connections, [], self.connections
            )
            for changed_socket in read_sockets:
                if changed_socket == self._socket:
                    client_socket, client_address = self._socket.accept()
                    self.connections.append(client_socket)
                    self.clients[client_socket] = client_address
                else:
                    data = changed_socket.recv(1024).decode()
                    if data:
                        return_message = self._database_wrapper.parse_message(data)
                        changed_socket.send(return_message.encode("utf-8"))
                    else:
                        self.clients.pop(changed_socket)
                        self.connections.remove(changed_socket)


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
