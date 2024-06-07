import sys

input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]


def sol():
    dp = [0] * (N + 1)
        
    for i, (t, p) in enumerate(table):
        for j in range(i + t, N + 1):
            dp[j] = max(dp[j], dp[i] + p)
            
    print(dp[N])


sol()
