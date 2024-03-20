def concat(start):
    result = start

    def execute(string=''):
        nonlocal result
        result += string
        return result

    return execute


builder = concat('a')
builder('b')
builder('c')
builder('d')

print(builder())
