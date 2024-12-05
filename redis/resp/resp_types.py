# class SimpleString:
#
#     def __init__(self, bytes_list):
#         self.bytes_list = bytes_list
#
#
# class Errors: ...
#
#
# class WholeNumbers: ...
#
#
# class BulkStrings:
#     def __init__(self, bytes_list):
#         self.bytes_list = bytes_list
#         self.simple_strings = SimpleString(bytes_list)
#
#
# class Tables:
#     def __init__(self, bytes_list):
#         self.bytes_list = bytes_list
#         self.bulk_strings = BulkStrings(self.bytes_list)
#

class Command:
    def __init__(self, bytes_list):
        self.bytes_list = bytes_list
        print(self.bytes_list)

    def validate(self):
        if self.bytes_list[0] != ord("*"):
            print("doesn't start with a star")
        
        ...

    def parse(self):
        ...
