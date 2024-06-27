def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0 if i == j else 2_000_000_000 for j in range(n)] for i in range(n)]
    
    for gap in range(1, n):
        for s in range(0, n - gap):
            e = s + gap
            for k in range(s, e):
                dp[s][e] = min(dp[s][e], dp[s][k] + dp[k + 1][e] + matrix_sizes[s][0] * matrix_sizes[e][1] * matrix_sizes[k + 1][0])
    
    return dp[0][-1]