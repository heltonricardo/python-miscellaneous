class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


def example_function(x):
    if x < 0:
        raise MyException("Input value cannot be negative")


try:
    example_function(-5)
except MyException as e:
    print("Caught MyException:", e)
