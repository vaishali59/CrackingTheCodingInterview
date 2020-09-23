def mul(a, b):

    # base cases
    if a == 0 or b == 0:
        return 0

    if b == 1:
        return a

    if a == 1:
        return b

    return a + mul(a, b - 1)


def multiply(a, b):
    if b<0:
        return -mul(a,-b)
    else:
        return mul(a,b)


if __name__ == '__main__':

    print(multiply(3, 4))
    print(multiply(-3, -4))
    print(multiply(-3, 4))
    print(multiply(3, -4))
