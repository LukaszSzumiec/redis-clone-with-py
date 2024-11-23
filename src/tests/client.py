import socket
from src.settings import SERVER_ADDRESS, PORT


class Client:
    @staticmethod
    def send(message: str):
        with socket.socket() as s:
            s.connect((SERVER_ADDRESS, PORT))
            s.sendall(message.encode())
            data = s.recv(1024)
            return data
