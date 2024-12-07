class ResponseSerializer:
    def __init__(self, return_message):
        self.message = return_message

    def serialize(self):
        if self.message == "NULL":
            return b'$-1\r\n'
        return f"${len(self.message)}\r\n{self.message}\r\n".encode()
