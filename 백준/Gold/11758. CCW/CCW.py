import sys

input = sys.stdin.readline

p1 = map(int, input().split())
p2 = map(int, input().split())
p3 = map(int, input().split())


def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0


def sol():
    print(ccw(p1, p2, p3))


sol()
