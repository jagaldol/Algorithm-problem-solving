import sys

input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    r, c = map(int, input().split())
    numbers.append(r)
    if i == N - 1:
        numbers.append(c)


def min_multiply(nums):
    n = len(nums)
    if n == 2:
        return 0
    if n == 3:
        return nums[0] * nums[1] * nums[2]
    nums[0] * nums[1] * nums[n - 1] + min_multiply(nums[1:])
    nums[0] * nums[2]
    result = 5_000_000_000
    for i in range(1, n - 1):
        result = min(result, nums[0] * nums[i] * nums[n - 1] + min_multiply(nums[: i + 1]) + min_multiply(nums[i:]))
    return result


def sol():
    n = len(numbers)
    dp = [[0] * n for _ in range(n + 1)]
    for i in range(n - 2):
        dp[3][i] = numbers[i] * numbers[i + 1] * numbers[i + 2]

    for i in range(4, n + 1):
        for j in range(n - i + 1):
            dp[i][j] = 5_000_000_000
            for k in range(1, i - 1):
                dp[i][j] = min(
                    dp[i][j], dp[k + 1][j] + dp[i - k][j + k] + numbers[j] * numbers[j + k] * numbers[j + i - 1]
                )

    print(dp[n][0])


sol()
