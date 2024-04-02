class Calculator:
    def __call__(self, x, y, operation):
        if operation == 'add':
            return x + y
        elif operation == 'subtract':
            return x - y
        elif operation == 'multiply':
            return x * y
        elif operation == 'divide':
            if y != 0:
                return x / y
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"


calc = Calculator()
print(calc(5, 3, 'add'))
print(calc(5, 3, 'subtract'))
print(calc(5, 3, 'multiply'))
print(calc(5, 3, 'divide'))
print(calc(5, 0, 'divide'))
print(calc(5, 3, 'power'))
