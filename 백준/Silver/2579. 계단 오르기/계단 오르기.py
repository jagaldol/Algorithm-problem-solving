import sys

input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]


def sol():
    if len(stairs) <= 2:
        print(sum(stairs))
        return

    dp = [0 for _ in range(N)]

    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[-1])


sol()
