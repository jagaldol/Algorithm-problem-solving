import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, (input().split()))
v = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(m)]

moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
max_value = 0


def dfs(step, x, y, current, value):
    if step == 3 and current == m - 1:
        global max_value
        if max_value < value + v[x][y]:
            max_value = value + v[x][y]
        return
    if step == 3:
        now = v[x][y]
        v[x][y] = 0
        dfs(
            0,
            starts[current + 1][0] - 1,
            starts[current + 1][1] - 1,
            current + 1,
            value + now,
        )
        v[x][y] = now
        return

    now = v[x][y]
    v[x][y] = 0
    for tx, ty in moves:
        if 0 <= x + tx < n and 0 <= y + ty < n:
            dfs(step + 1, x + tx, y + ty, current, value + now)
    v[x][y] = now


dfs(0, starts[0][0] - 1, starts[0][1] - 1, 0, 0)

print(max_value)
