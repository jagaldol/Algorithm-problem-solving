def solution(triangle):
    dp = [row[:] for row in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j- 1], dp[i - 1][j])
                
    return max(dp[len(triangle) - 1])