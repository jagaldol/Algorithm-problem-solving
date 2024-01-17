import sys


def sol():
    input = sys.stdin.readline

    C, N = map(int, input().split())

    cities = [list(map(int, input().split())) for _ in range(N)]

    dp = [100_000_000 for _ in range(C + 100)]

    dp[0] = 0

    for cost, customer_num in cities:
        for i in range(customer_num, C + 100):
            dp[i] = min(dp[i - customer_num] + cost, dp[i])

    print(min(dp[C:]))


sol()
