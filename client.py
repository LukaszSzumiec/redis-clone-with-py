import socket

s = socket.socket()

port = 12345
host = socket.gethostname()
s.connect((host, port))

print(s.recv(1024).decode())
s.close()
