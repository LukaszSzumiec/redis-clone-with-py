from redis.resp.resp_types import Command


class ValidateRequest:
    def __init__(self, data: bytes):
        print(f"INPUT COMMAND: {data}")
        self.input_data = data
        self.bytes_list = [x for x in data]

    def validate(self):
        command = Command(self.bytes_list)
        command.validate()
        command.parse()
        # amount_of_bulk_strings = self._find_amount_of_bulked_strings()
        # if self.is_table():
        #     print("1")
        # elif self.
        # else:
        #     print("2")

    def _find_amount_of_bulked_strings(self):
        control_star = self.input_data[0]
        elements_amount = self.input_data[1]
        print("CONTROL STAR: ", control_star)
        print(ord("*"))
        if control_star != ord("*"):
            print("Nie zaczyna sie od gwiazdki.")
            raise Exception

        return elements_amount


    def is_a_list_of_commands(self):
        ...
