import math
import sys

input = sys.stdin.readline
N = int(input())

shirts = map(int, input().split())
t, p = map(int, input().split())


def sol():
    print(sum(math.ceil(shirt / t) for shirt in shirts))
    print(N // p, N % p)


sol()
