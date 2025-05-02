N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)]


def tsp(current, status):
    if status == (1 << N) - 1:
        return W[current][0] if W[current][0] != 0 else float("inf")
    if dp[current][status] != 0:
        return dp[current][status]

    dp[current][status] = float("inf")
    for j in range(N):
        if not status & (1 << j) and W[current][j] != 0:
            dp[current][status] = min(dp[current][status], W[current][j] + tsp(j, status | (1 << j)))
    return dp[current][status]


print(tsp(0, 1))
