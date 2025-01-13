import sys

input = sys.stdin.readline

n = int(input())
levels = [int(input()) for _ in range(n)]


def my_round(n):
    return int(n + 0.5)


def sol():
    if n == 0:
        print(0)
        return
    cut = my_round(n * 0.15)
    print(my_round(sum(sorted(levels)[cut : n - cut]) / (n - 2 * cut)))


sol()
