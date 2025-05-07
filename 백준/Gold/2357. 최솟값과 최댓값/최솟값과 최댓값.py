import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]

tree = [0] * (4 * N)


def build(node, start, end):
    if start == end:
        tree[node] = (A[start], A[start])
        return
    mid = (start + end) // 2

    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)

    min_value = min(tree[node * 2][0], tree[node * 2 + 1][0])
    max_value = max(tree[node * 2][1], tree[node * 2 + 1][1])
    tree[node] = (min_value, max_value)


def query(node, start, end, left, right):
    if right < start or end < left:
        return (float("inf"), float("-inf"))

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_min, left_max = query(node * 2, start, mid, left, right)
    right_min, right_max = query(node * 2 + 1, mid + 1, end, left, right)

    return (min(left_min, right_min), max(left_max, right_max))


build(1, 1, N)


for _ in range(M):
    a, b = map(int, input().split())
    print(*query(1, 1, N, a, b))
