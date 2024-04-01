import sys

sys.setrecursionlimit(10**6)

visited = []
moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
food = 0


def dfs(maps, x, y):
    if maps[x][y] == "X":
        return
    global food
    food += int(maps[x][y])

    for tx, ty in moves:
        nx, ny = x + tx, y + ty
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(maps, nx, ny)


def solution(maps):
    global visited
    visited = [[False for _ in maps[0]] for _ in maps]

    answer = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j]:
                global food
                food = 0
                visited[i][j] = True
                dfs(maps, i, j)
                if food != 0:
                    answer.append(food)

    return sorted(answer) if len(answer) > 0 else [-1]
