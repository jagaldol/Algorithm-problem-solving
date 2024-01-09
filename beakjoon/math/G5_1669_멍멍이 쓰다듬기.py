import math


def sol():
    X, Y = map(int, input().split())

    if X == Y:
        print(0)
        return

    print(math.ceil((Y - X) ** 0.5 * 2 - 1))


sol()
