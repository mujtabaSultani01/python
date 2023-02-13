"""
User Defined Exception or custom exception is creating your own exception class and throws that exception using
'throw' keyword.
"""


class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception:", self.msg)


try:
    raise Accident("Crush between two cars.")
except Accident as e:
    e.print_exception()
