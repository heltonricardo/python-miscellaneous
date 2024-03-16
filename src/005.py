def zipper(list1, list2):
    size = min(len(list1), len(list2))

    return [
        (list1[i], list2[i])
        for i in range(size)
    ]


cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
abbreviations = ['BA', 'SP', 'MG', 'RJ']

union = zipper(cities, abbreviations)

print(union)
