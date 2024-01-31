import sys


def to_coordinate(n: str, d):
    x, y = 0, 0

    for level in range(d):
        position = n[level]
        modifier = 2 ** (d - 1 - level)

        if position == "1":
            x += modifier
            y += modifier
        elif position == "2":
            y += modifier
        elif position == "3":
            pass
        elif position == "4":
            x += modifier
    return x, y


def to_value(x, y, d):
    value = ""

    for level in range(d - 1, -1, -1):
        divider = 2**level

        quotient_x = x // divider
        quotient_y = y // divider

        if quotient_x == 1 and quotient_y == 1:
            value += "1"
        elif quotient_x == 1:
            value += "4"
        elif quotient_y == 1:
            value += "2"
        else:
            value += "3"

        x = x % divider
        y = y % divider

    return value


def sol():
    input = sys.stdin.readline

    d, n = map(int, input().split())
    x, y = map(int, input().split())

    ox, oy = to_coordinate(str(n), d)

    nx, ny = ox + x, oy + y

    if 0 <= nx < 2**d and 0 <= ny < 2**d:
        print(to_value(nx, ny, d))
    else:
        print(-1)


sol()
