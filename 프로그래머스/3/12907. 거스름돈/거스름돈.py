def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    money.sort()
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
            dp[i] %= 1_000_000_007
    
    return dp[n]
