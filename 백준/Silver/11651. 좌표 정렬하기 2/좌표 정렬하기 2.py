import sys

input = sys.stdin.readline

N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]


def sol():
    new_positions = [(y, x) for x, y in positions]
    new_positions.sort()
    for y, x in new_positions:
        print(x, y)


sol()
