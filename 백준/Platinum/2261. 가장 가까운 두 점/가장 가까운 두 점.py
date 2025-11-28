import sys

input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()


def find_min_dist(start, end):
    if end - start <= 2:
        min_dist = float("inf")
        for i in range(start, end + 1):
            for j in range(i + 1, end + 1):
                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                min_dist = min(min_dist, dist)
        return min_dist

    mid = (start + end) // 2
    left = find_min_dist(start, mid)
    right = find_min_dist(mid + 1, end)

    min_dist = min(left, right)

    mid_x = points[mid][0]
    strip = []
    for point in points[start : end + 1]:
        if (point[0] - mid_x) ** 2 < min_dist:
            strip.append(point)
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            dy = strip[j][1] - strip[i][1]
            if dy * dy >= min_dist:
                break
            dist = (strip[i][0] - strip[j][0]) ** 2 + (strip[i][1] - strip[j][1]) ** 2
            min_dist = min(min_dist, dist)
    return min_dist


print(find_min_dist(0, n - 1))
