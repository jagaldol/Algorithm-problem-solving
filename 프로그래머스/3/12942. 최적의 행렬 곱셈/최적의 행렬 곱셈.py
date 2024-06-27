def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for gap in range(0, n):
        for s in range(0, n - gap):
            e = s + gap
            if s == e:
                continue
            dp[s][e] = 2_000_000_000
            for k in range(s, e):
                dp[s][e] = min(dp[s][e], dp[s][k] + dp[k + 1][e] + matrix_sizes[s][0] * matrix_sizes[e][1] * matrix_sizes[k + 1][0])
    
    return dp[0][n - 1]