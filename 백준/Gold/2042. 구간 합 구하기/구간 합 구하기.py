import bisect
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

MIN_INFINITY = float("-inf")

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + A[i]

change_logs = []

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = bisect.bisect_left(change_logs, (b, MIN_INFINITY))
        if idx < len(change_logs) and change_logs[idx][0] == b:
            change_logs[idx] = (b, c)
        else:
            change_logs.insert(idx, (b, c))
    else:
        answer = dp[c] - dp[b - 1]

        left = bisect.bisect_left(change_logs, (b, MIN_INFINITY))
        right = bisect.bisect_right(change_logs, (c, float("inf")))

        for i in range(left, right):
            idx, value = change_logs[i]
            answer = answer - A[idx] + value
        print(answer)
