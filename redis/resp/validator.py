class ValidateRequest:
    def __init__(self, data: bytes):
        print(f"INPUT COMMAND: {data}")
        self.input_data = data
        self.bytes_list = [x for x in data]

    def validate(self):
        if self.is_a_list_of_commands():
            print("1")
        # elif self.
        else:
            print("2")

    def is_a_list_of_commands(self):
        if len(self.bytes_list) and self.bytes_list[0] == 42:
            return True
        else:
            return False
