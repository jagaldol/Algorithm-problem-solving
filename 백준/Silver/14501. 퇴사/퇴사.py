import sys

input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]


def sol():
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]
        for j in range(1, i + 1):
            if table[i - j][0] <= j:
                dp[i] = max(dp[i - j] + table[i - j][1], dp[i])

    print(dp[N])


sol()
