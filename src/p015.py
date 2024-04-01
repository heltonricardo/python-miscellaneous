def number_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


generator = number_generator(1, 5)
for num in generator:
    print(num)
