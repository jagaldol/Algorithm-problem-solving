N = int(input())

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N)]

for j in range(1, 10):
    dp[0][j][2**j] = 1

mod = 1_000_000_000
for i in range(1, N):
    for j in range(10):
        for mask in range(1024):
            if j > 0:
                dp[i][j][mask | 2**j] += dp[i - 1][j - 1][mask]
            if j < 9:
                dp[i][j][mask | 2**j] += dp[i - 1][j + 1][mask]
            dp[i][j][mask | 2**j] %= mod

print(sum(dp[N - 1][j][1023] for j in range(10)) % mod)
