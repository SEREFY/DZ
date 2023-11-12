result = []
def divider(a, b):
    try:
        if a < b:
            try:
                return  a
            except ValueError:
                print(ValueError)
                return b
    except TypeError:
        print(TypeError)
        return b
    if b > 100:
        raise IndexError
    try:
        return a/b
    except ZeroDivisionError:
        print(ZeroDivisionError)
        return a

data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8 : 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

    print(result)