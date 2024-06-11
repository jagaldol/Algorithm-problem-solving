import sys


def to_coordinate(n: str, d, idx, x, y):
    if idx == d:
        return x, y

    position = n[idx]
    modifier = 2 ** (d - 1 - idx)

    if position == "1":
        return to_coordinate(n, d, idx + 1, x + modifier, y + modifier)
    elif position == "2":
        return to_coordinate(n, d, idx + 1, x, y + modifier)
    elif position == "3":
        return to_coordinate(n, d, idx + 1, x, y)
    elif position == "4":
        return to_coordinate(n, d, idx + 1, x + modifier, y)


def to_value(x, y, level):
    if level == -1:
        return ""

    divider = 2**level
    quotient_x = x // divider
    quotient_y = y // divider

    if quotient_x == 1 and quotient_y == 1:
        return "1" + to_value(x % divider, y % divider, level - 1)
    elif quotient_x == 1:
        return "4" + to_value(x % divider, y % divider, level - 1)
    elif quotient_y == 1:
        return "2" + to_value(x % divider, y % divider, level - 1)
    else:
        return "3" + to_value(x % divider, y % divider, level - 1)


def sol():
    input = sys.stdin.readline

    d, n = map(int, input().split())
    x, y = map(int, input().split())

    ox, oy = to_coordinate(str(n), d, 0, 0, 0)

    nx, ny = ox + x, oy + y

    if 0 <= nx < 2**d and 0 <= ny < 2**d:
        print(to_value(nx, ny, d - 1))
    else:
        print(-1)


sol()
