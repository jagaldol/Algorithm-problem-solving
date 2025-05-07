import sys

input = sys.stdin.readline
n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]
d = int(input())
contained = [0] * n


def sol():
    points = []
    for idx, (h, o) in enumerate(positions):
        points.append((h, idx))
        points.append((o, idx))

    points.sort()
    answer = 0
    left = 0
    right = 0
    count = 0
    while left < n * 2:
        start = points[left][0]
        end = start + d
        while right < n * 2 and points[right][0] <= end:
            contained[points[right][1]] += 1
            if contained[points[right][1]] == 2:
                count += 1
            right += 1
        answer = max(answer, count)
        if contained[points[left][1]] == 2:
            count -= 1
        contained[points[left][1]] -= 1
        left += 1
    print(answer)


sol()
