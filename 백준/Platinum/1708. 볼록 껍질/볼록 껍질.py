import math
import sys

input = sys.stdin.readline
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


def ccw(p1, p2, p3):
    u = (p2[0] - p1[0], p2[1] - p1[1])
    v = (p3[0] - p1[0], p3[1] - p1[1])
    return u[0] * v[1] - u[1] * v[0]


points.sort()
base = points[0]
points = sorted(points[1:], key=lambda p: math.atan2(p[1] - base[1], p[0] - base[0]))

stack = [base]
for p in points:
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], p) <= 0:
        stack.pop()
    stack.append(p)

print(len(stack))
