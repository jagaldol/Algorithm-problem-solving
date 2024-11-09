import sys

input = sys.stdin.readline


def cantor(n: int):
    if n == 0:
        print("-", end="")
        return

    cantor(n - 1)
    for _ in range(3 ** (n - 1)):
        print(" ", end="")
    cantor(n - 1)


def sol():
    while True:
        try:
            cantor(int(input()))
            print()
        except Exception:
            break


sol()
