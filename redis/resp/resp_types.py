class SimpleString: ...


class Errors: ...


class WholeNumbers: ...


class BulkStrings:
    def __init__(self, bytes_list):
        self.bytes_list = bytes_list


class Tables:
    def __init__(self, bytes_list):
        self.bytes_list = bytes_list
        self.bulk_strings = BulkStrings(self.bytes_list)


class Command:
    def __init__(self, bytes_list):
        self.bytes_list = bytes_list
        self.tables = Tables(self.bytes_list)

    def build(self):
        ...

    def parse(self):
        ...
