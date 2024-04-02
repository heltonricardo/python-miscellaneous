class Multiplier:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplier
        return inner


@Multiplier(10)
def addition(x, y):
    return x + y


result = addition(13, 29)
print(result)
