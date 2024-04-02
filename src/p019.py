class Calculator:
    def __init__(self):
        self.operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else "Cannot divide by zero",
            'invalid': lambda *_: "Invalid operation"
        }

    def __call__(self, x, y, operation):
        return self.operations.get(operation, self.operations['invalid'])(x, y)


calc = Calculator()

result = calc(5, 3, 'add')
print(result)

result = calc(5, 3, 'subtract')
print(result)

result = calc(5, 3, 'multiply')
print(result)

result = calc(5, 3, 'divide')
print(result)

result = calc(5, 0, 'divide')
print(result)

result = calc(5, 3, 'power')
print(result)
