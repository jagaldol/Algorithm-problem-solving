import sys

input = sys.stdin.readline

N, K = map(int, input().split())
objects = [list(map(int, input().split())) for _ in range(N)]


def sol():
    dp = [[0] * (N) for _ in range(K + 1)]
    for i in range(K + 1):
        W, V = objects[0]
        if i - W >= 0:
            dp[i][0] = V

    for i in range(K + 1):
        for j in range(1, N):
            W, V = objects[j]
            if i - W >= 0:
                dp[i][j] = max(dp[i - W][j - 1] + V, dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    print(max(dp[-1]))


sol()
