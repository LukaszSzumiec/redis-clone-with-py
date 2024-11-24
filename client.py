import socket

from redis.settings import SERVER_ADDRESS, PORT


class QuickClient:
    @staticmethod
    def connect_and_send(message: str):
        with socket.socket() as s:
            s.connect((SERVER_ADDRESS, PORT))
            s.sendall(message.encode())
            data = s.recv(1024)
            return data


class SeparatedClient:
    def __enter__(self):
        self.s = socket.socket()
        self.s.connect((SERVER_ADDRESS, PORT))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s.close()

    def send(self, message):
        self.s.sendall(message.encode())
        data = self.s.recv(1024)
        return data


if __name__ == "__main__":
    print("Client is starting...")
    with SeparatedClient() as client:
        while True:
            query = input("Parse query: ")
            response = client.send(query)
            print(response)
