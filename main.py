import socket


def connect(s):
    while True:
        c, addr = s.accept()
        try:
            print('Got connection from', addr)
            c.send('Buziaczki'.encode())
        finally:
            c.close()


def setup():
    s = socket.socket()
    print("Socket successfully created")
    port = 12345
    host = socket.gethostname()

    s.bind((host, port))
    print("socket binded to %s" % (port))

    s.listen(1)
    print("socket is listening")
    connect(s)


setup()
