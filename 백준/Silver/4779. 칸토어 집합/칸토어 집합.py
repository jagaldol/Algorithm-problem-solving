import sys

sys.setrecursionlimit(10**5)


def cantor(n: int):
    if n == 0:
        return "-"

    child = cantor(n - 1)
    return child + " " * (3 ** (n - 1)) + child


def sol():
    for line in sys.stdin:
        print(cantor(int(line)))


sol()
