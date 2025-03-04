import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
costs = [[-1] * m for _ in range(n)]


def sol():
    s_x, s_y = ((i, j) for i in range(n) for j in range(m) if board[i][j] == 2).__next__()
    costs[s_x][s_y] = 0

    queue = deque([(s_x, s_y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and costs[nx][ny] == -1:
                costs[nx][ny] = costs[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            cost = costs[i][j]
            if cost == -1 and board[i][j] == 0:
                cost = 0
            print(cost, end=" ")
        print()


sol()
