A = input()
B = input()


def sol():
    N = len(A)
    M = len(B)
    dp = [[""] * M for _ in range(N)]

    if A[0] == B[0]:
        dp[0][0] = A[0]

    for i in range(1, M):
        if A[0] == B[i]:
            dp[0][i] = A[0]
        else:
            dp[0][i] = dp[0][i - 1]

    for i in range(1, N):
        if A[i] == B[0] and len(dp[i - 1][0]) == 0:
            dp[i][0] = A[i]
        else:
            dp[i][0] = dp[i - 1][0]
        for j in range(1, M):
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

            if A[i] == B[j]:
                if len(dp[i - 1][j - 1]) + 1 > len(dp[i][j]):
                    dp[i][j] = dp[i - 1][j - 1] + A[i]

    print(len(dp[N - 1][M - 1]))
    print(dp[N - 1][M - 1])


sol()
