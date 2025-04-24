import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline
T = int(input())


def construct(D, tree, costs, node):
    if costs[node] != -1:
        return costs[node]
    if not tree[node]:
        cost = D[node]
    else:
        cost = max(construct(D, tree, costs, child) for child in tree[node]) + D[node]
    costs[node] = cost
    return cost


def sol():
    for _ in range(T):
        N, K = map(int, input().split())
        D = [0] + list(map(int, input().split()))
        tree = [[] for _ in range(N + 1)]
        costs = [-1] * (N + 1)
        for _ in range(K):
            X, Y = map(int, input().split())
            tree[Y].append(X)
        target = int(input())

        print(construct(D, tree, costs, target))


sol()
