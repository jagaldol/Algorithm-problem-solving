import sys

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


def sol():
    for x, y in data:
        print(sum(1 for ox, oy in data if ox > x and oy > y) + 1)


sol()
