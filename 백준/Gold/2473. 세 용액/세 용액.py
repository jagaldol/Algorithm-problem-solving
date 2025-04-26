import sys

input = sys.stdin.readline
N = int(input())
items = list(map(int, input().split()))
items.sort()


def sol():
    answer = (1_000_000_0000, 1_000_000_0000, 1_000_000_0000)
    for min_base in range(N - 2):
        left = min_base + 1
        right = N - 1
        while left < right:
            total = items[min_base] + items[left] + items[right]
            if abs(total) < abs(sum(answer)):
                answer = (items[min_base], items[left], items[right])
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                break

    print(*answer)


sol()
