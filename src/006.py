from itertools import zip_longest

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

list_sum_1 = [
    x + y
    for x, y in zip(list_a, list_b)
]

list_sum_2 = [
    x + y
    for x, y in zip_longest(
        list_a,
        list_b,
        fillvalue=0
    )
]

print(list_sum_1)
print(list_sum_2)
