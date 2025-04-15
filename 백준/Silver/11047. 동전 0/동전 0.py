import bisect
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]


def sol():
    answer = 0

    remain = K

    while remain > 0:
        idx = bisect.bisect(values, remain)
        if idx == 0:
            break
        answer += remain // values[idx - 1]
        remain %= values[idx - 1]
    print(answer)


sol()
