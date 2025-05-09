import sys

input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())

tree = [0] * (4 * N)
MOD = 10**9 + 7


def build(node, start, end):
    if start == end:
        tree[node] = (A[start], start)
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])


def update(node, start, end, idx, value):
    if start == end:
        A[idx] = value
        tree[node] = (value, idx)
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(node * 2, start, mid, idx, value)
        else:
            update(node * 2 + 1, mid + 1, end, idx, value)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])


def query(node, start, end, left, right):
    if right < start or end < left:
        return (float("inf"), float("inf"))
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_min = query(node * 2, start, mid, left, right)
    right_min = query(node * 2 + 1, mid + 1, end, left, right)
    return min(left_min, right_min)


build(1, 1, N)

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
    else:
        print(query(1, 1, N, b, c)[1])
