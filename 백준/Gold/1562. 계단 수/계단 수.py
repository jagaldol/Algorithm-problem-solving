N = int(input())

MOD = 1_000_000_000
types = [(1, 10), (1, 9), (2, 10), (2, 9)]
dp = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
]

for _ in range(N - 1):
    for i, (s, e) in enumerate(types):
        tmp_dp = dp[i][:]
        for j in range(s, e + 1):
            tmp_dp[j] = (dp[i][j - 1] + dp[i][j + 1]) % MOD
        dp[i] = tmp_dp


print((sum(dp[0]) - sum(dp[1]) - sum(dp[2]) + sum(dp[3])) % MOD)
