import sys

input = sys.stdin.readline

N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]


def get_triangle_area(a, b, c):
    return ((a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])) / 2


def sol():
    area = 0
    for i in range(N - 2):
        area += get_triangle_area(positions[0], positions[i + 1], positions[i + 2])
    area = round(abs(area), 1)
    print(area)


sol()
