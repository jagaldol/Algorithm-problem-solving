import sys


def sol():
    input = sys.stdin.readline

    A = input().rstrip()
    B = input().rstrip()

    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    print(dp[len(A)][len(B)])


sol()
