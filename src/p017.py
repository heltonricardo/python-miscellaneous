from contextlib import contextmanager


@contextmanager
def file_writer(file_name):
    try:
        file = open(file_name, "w", encoding="utf8")
        yield file
    finally:
        file.close()


with file_writer("example.txt") as file:
    file.write("Hello, world!\nThis is a test.")
