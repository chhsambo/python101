def test(x):
    return x * 10


def divide(x, y):
    x = test(x)
    result = x // y
    remain = x % y
    return result, remain


a, b = divide(10, 3)
print(a)
print(b)
