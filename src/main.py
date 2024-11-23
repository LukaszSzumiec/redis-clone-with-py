import socket
import queue
from src.settings import SERVER_ADDRESS, PORT


client_queue = queue.Queue()


def process_queue():
    while True:
        client_socket, client_address = client_queue.get()  # Pobiera klienta z kolejki
        handle_client(client_socket, client_address)
        client_queue.task_done()


class TCPServer:
    def __init__(self):
        self._socket = socket.socket()
        self._database_wrapper = DatabaseWrapper()

    def __enter__(self):
        self._socket.bind((SERVER_ADDRESS, PORT), )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def listen_for_requests(self):
        while True:
            self._socket.listen(5)
            connection, address = self._socket.accept()
            message = connection.recv(1024).decode()
            print(f"Received message: {message}")

            return_message = self._database_wrapper.parse_message(message)

            connection.send(return_message.encode())
            connection.close()

    def handle_request(self, client_socket, client_address):
        try:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Otrzymano od {client_address}: {data}")
            response = f"Serwer otrzymał: {data}"
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Błąd obsługi klienta {client_address}: {e}")
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
