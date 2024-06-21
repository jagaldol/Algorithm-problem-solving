import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def main():
    dp = [[one for one in row] for row in board]

    for i in range(1, n):
        dp[0][i] += dp[0][i - 1]
        dp[i][0] += dp[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])

    dp2 = [[one for one in row] for row in board]

    dp2[0][0] *= 2

    for i in range(1, n):
        dp2[0][i] += max(dp[0][i], dp2[0][i - 1])
        dp2[i][0] += max(dp[i][0], dp2[i - 1][0])

    for i in range(1, n):
        for j in range(1, n):
            dp2[i][j] += max(dp2[i - 1][j], dp2[i][j - 1], dp[i][j])
    print(dp2[-1][-1])


main()
