import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]


def sol():
    for i, num in enumerate(numbers):
        dp[i + 1] = dp[i] + num
    for _ in range(M):
        i, j = map(int, input().split())
        print(dp[j] - dp[i - 1])


sol()
