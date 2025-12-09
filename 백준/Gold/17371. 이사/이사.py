import sys

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


answer = None
min_sum = float("inf")

for point1 in points:
    max_dist = 0
    for point2 in points:
        dist = distance(point1, point2)
        max_dist = max(max_dist, dist)

    if max_dist < min_sum:
        min_sum = max_dist
        answer = point1


print(*answer)
