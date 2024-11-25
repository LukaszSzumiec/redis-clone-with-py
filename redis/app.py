import socket
import queue
import select
from redis.settings import SERVER_ADDRESS, PORT, MAX_CLIENTS


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
            for connection in read_sockets:
                if connection == self._socket:
                    self.accept_new_connection()
                else:
                    self.handle_request(connection=connection)

    def accept_new_connection(self):
        client_socket, client_address = self._socket.accept()
        self.connections.append(client_socket)
        self.clients[client_socket] = client_address
        print("New connection accepted")

    def handle_request(self, connection):
        data = connection.recv(1024).decode()
        if data:
            try:
                print(f"Received message {str(data)}")
                return_message = self._database_wrapper.parse_message(data)
                if not return_message:
                    connection.send("Syntax Error".encode())
                else:
                    connection.send(return_message.encode())
            except Exception as e:
                connection.send(f"Exception Occured {str(e)}".encode())
        else:
            print("Connection with client closed")
            self.clients.pop(connection)
            self.connections.remove(connection)


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
