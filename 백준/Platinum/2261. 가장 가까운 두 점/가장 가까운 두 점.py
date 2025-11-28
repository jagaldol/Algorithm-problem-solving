import sys

input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()

for i in range(1, n):
    if points[i] == points[i - 1]:
        print(0)
        sys.exit(0)

def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

def find_min_dist(start, end):
    if end - start <= 2:
        min_dist = float("inf")
        for i in range(start, end + 1):
            for j in range(i + 1, end + 1):
                d = dist2(points[i], points[j])
                if d < min_dist:
                    min_dist = d
        return min_dist

    mid = (start + end) // 2
    left = find_min_dist(start, mid)
    right = find_min_dist(mid + 1, end)

    min_dist = min(left, right)

    mid_x = points[mid][0]
    strip = []
    for i in range(start, end + 1):
        px, py = points[i]
        dx = px - mid_x
        if dx * dx < min_dist:
            strip.append(points[i])
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            dy = strip[j][1] - strip[i][1]
            if dy * dy >= min_dist:
                break
            d = dist2(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
    return min_dist


print(find_min_dist(0, n - 1))
