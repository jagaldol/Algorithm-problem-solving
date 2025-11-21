import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())


def sol():
    dist1 = x
    dist2 = w - x
    dist3 = y
    dist4 = h - y
    print(min(dist1, dist2, dist3, dist4))


sol()
