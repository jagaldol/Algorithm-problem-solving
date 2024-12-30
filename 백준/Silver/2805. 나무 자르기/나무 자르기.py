import bisect
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]


def calculate(h):
    low_tree_index = bisect.bisect_left(trees, h)
    return dp[N] - dp[low_tree_index] - (N - low_tree_index) * h


def parametric(s, e):
    if s > e:
        print(e)
        return
    mid = (s + e) // 2
    if M <= calculate(mid):
        parametric(mid + 1, e)
    else:
        parametric(s, mid - 1)


def sol():
    trees.sort()
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + trees[i - 1]
    calculate(5)

    parametric(1, trees[N - 1])


sol()
