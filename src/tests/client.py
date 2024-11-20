import socket


class Client:
    @staticmethod
    def send(message: str):
        with socket.socket() as s:
            s.connect((socket.gethostname(), 12345))
            s.sendall(message.encode())
            data = s.recv(1024)
            return data
