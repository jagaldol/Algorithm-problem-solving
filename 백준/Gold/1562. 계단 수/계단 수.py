N = int(input())
MOD = 1_000_000_000


def step_dp(s, e):
    s += 1
    e += 1

    dp = [[0 for _ in range(12)] for _ in range(N)]

    for j in range(max(s, 2), e + 1):
        dp[0][j] = 1

    for i in range(1, N):
        for j in range(s, e + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

    return sum(dp[N - 1]) % MOD


print((step_dp(0, 9) - (step_dp(0, 8) + step_dp(1, 9) - step_dp(1, 8))) % MOD)
