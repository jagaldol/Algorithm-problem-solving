import bisect
import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
items = list(map(int, input().split()))
items.sort()


def sol():
    lowest = 5_000_000_0000
    answer = [0, 0, 0]
    for a, b in combinations(items, 2):
        pair_sum = a + b
        i = bisect.bisect(items, -pair_sum)

        right = i
        while right < N and items[right] in (a, b):
            right += 1
        if right < N and abs(items[right] + pair_sum) < lowest:
            lowest = abs(items[right] + pair_sum)
            answer[0] = items[right]
            answer[1] = a
            answer[2] = b

        left = i - 1
        while left >= 0 and items[left] in (a, b):
            left -= 1
        if left >= 0 and abs(items[left] + pair_sum) < lowest:
            lowest = abs(items[left] + pair_sum)
            answer[0] = items[left]
            answer[1] = a
            answer[2] = b

    print(*sorted(answer))


sol()
