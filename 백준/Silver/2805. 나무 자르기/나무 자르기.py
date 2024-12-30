import bisect
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
dp = [0 for _ in range(N)]


def calculate(h):
    # low_tree_index = bisect.bisect_left(trees, h)
    # return dp[N - 1] - dp[low_tree_index - 1] - (N - low_tree_index) * h
    return sum(max(tree - h, 0) for tree in trees)


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
    # dp[0] = trees[0]
    # for i in range(1, N):
    #     dp[i] = trees[i] + dp[i - 1]

    parametric(1, trees[N - 1])


sol()
