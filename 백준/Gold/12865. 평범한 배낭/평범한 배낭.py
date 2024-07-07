import sys

input = sys.stdin.readline

N, K = map(int, input().split())
objects = [list(map(int, input().split())) for _ in range(N)]


def sol():
    dp = [0] * (K + 1)

    for W, V in objects:
        for i in range(K, W - 1, -1):
            dp[i] = max(dp[i], dp[i - W] + V)

    print(dp[-1])


sol()
