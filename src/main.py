import socket
import threading

import queue
from src.settings import SERVER_ADDRESS, PORT, MAX_CLIENTS


class TCPServer:
    def __init__(self):
        self._socket = socket.socket()
        self._database_wrapper = DatabaseWrapper()
        self.client_queue = queue.Queue()

    def __enter__(self):
        self._socket.bind(
            (SERVER_ADDRESS, PORT),
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def listen_for_requests(self):
        threading.Thread(target=self.process_queue, daemon=True).start()

        while True:
            self._socket.listen(MAX_CLIENTS)
            client_socket, client_address = self._socket.accept()
            self.client_queue.put((client_socket, client_address))

    def process_queue(self):
        while True:
            client_socket, client_address = self.client_queue.get()
            self.handle_request(client_socket, client_address)
            self.client_queue.task_done()

    def handle_request(self, client_socket, client_address):
        try:
            data = client_socket.recv(1024).decode("utf-8")
            return_message = self._database_wrapper.parse_message(data)
            client_socket.send(return_message.encode("utf-8"))
        except Exception as e:
            print(f"Client handling error: {client_address}: {e}")
        finally:
            client_socket.close()


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
