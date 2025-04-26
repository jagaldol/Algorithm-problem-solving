N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))


def sol():
    max_cost = sum(costs)
    dp = [[0 for _ in range(max_cost + 1)] for _ in range(N + 1)]
    result = 100_000

    for i in range(1, N + 1):
        memory = memories[i - 1]
        cost = costs[i - 1]

        for j in range(max_cost + 1):
            dp[i][j] = dp[i - 1][j]
            if j - cost >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - cost] + memory)

            if dp[i][j] >= M:
                result = min(result, j)

    print(result)


sol()
