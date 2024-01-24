def sol():
    N, K = map(int, input().split())

    num = input().rstrip()

    dp = ["9"] * N

    max_value = 0
    for idx, n in enumerate(num):
        max_value = max(int(n), max_value)
        if max_value == 9:
            break
        dp[idx] = str(max_value)

    temp = ""
    for i in range(1, N - K):
        temp = "0"
        for j in range(i, N):
            temp, dp[j - 1] = max(dp[j - 1] + num[j], temp), temp

    print(temp)


sol()
