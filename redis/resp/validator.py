class ValidateRequest:
    SUPPORTED_COMMANDS = [
        "GET",
        "SET",
        "DEL",
        "LPUSH",
        "COMMAND",
    ]

    def __init__(self, data: bytes):
        self.input_data = data
        self.bytes_list = [x for x in data]

    def validate(self):
        bytes_list_iter = iter(self.bytes_list)

        if next(bytes_list_iter) != ord("*"):
            print("doesn't start with a star")

        arguments_amount = int(chr(next(bytes_list_iter)))

        if 0 > arguments_amount > 10:
            print("arguments amount is invalid: %d", arguments_amount)

        _ = next(bytes_list_iter)
        _ = next(bytes_list_iter)

        command = []
        for i in range(arguments_amount):
            command.append(self.handle_a_word(bytes_list_iter))

        self._validate_command(command[0])

        return command

    @classmethod
    def handle_a_word(cls, bytes_list_iter):
        if next(bytes_list_iter) != ord("$"):
            print("no $")

        chars_in_bulk_string = int(chr(next(bytes_list_iter)))
        print(chars_in_bulk_string)

        _ = next(bytes_list_iter)
        _ = next(bytes_list_iter)

        word = []
        for i in range(chars_in_bulk_string):
            word.append(chr(next(bytes_list_iter)))

        _ = next(bytes_list_iter)
        _ = next(bytes_list_iter)
        return "".join(word)

    @classmethod
    def _validate_command(cls, command_word):
        if command_word not in cls.SUPPORTED_COMMANDS:
            raise Exception("command not supported %s", command_word)
