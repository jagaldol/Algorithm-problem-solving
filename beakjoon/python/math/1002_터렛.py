import sys
import math


def available_position_num(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if dist == 0 and r1 == r2:
        return -1
    if r1 + r2 == dist or dist == abs(r1 - r2):
        return 1
    if r1 + r2 > dist and dist > abs(r1 - r2):
        return 2
    return 0


def sol():
    input = sys.stdin.readline

    T = int(input())

    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        print(available_position_num(x1, y1, r1, x2, y2, r2))


sol()
