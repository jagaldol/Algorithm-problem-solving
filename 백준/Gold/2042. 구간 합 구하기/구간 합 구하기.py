import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]

tree = [0] * (4 * N)


def build(node, start, end):
    if start == end:
        tree[node] = A[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(node, start, end, idx, value):
    if start == end:
        A[idx] = value
        tree[node] = value
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(node * 2, start, mid, idx, value)
        else:
            update(node * 2 + 1, mid + 1, end, idx, value)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)


build(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
    else:
        print(query(1, 1, N, b, c))
