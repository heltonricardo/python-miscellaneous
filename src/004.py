def only_numbers(func):

    def inner(*args):
        if not all(isinstance(a, (int, float)) for a in args):
            raise TypeError("This function only accepts numbers")
        return func(*args)

    return inner


@only_numbers
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 4, "5"))
