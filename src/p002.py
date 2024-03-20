def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def execute(func, *args):
    def calculate(value):
        return func(value, *args)
    return calculate


add_five = execute(add, 5)
multiply_ten = execute(multiply, 10)

print(add_five(8))
print(multiply_ten(30))
