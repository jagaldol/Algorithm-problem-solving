import sys

input = sys.stdin.readline

N = int(input())
colors = [list(map(int, input().split())) for _ in range(3 * N)]
garage = [[[] for _ in range(N)] for _ in range(3)]

answer = 0

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
neighbors = []


def dfs(round, visited, i, j, target):
    neighbors.append((i, j))
    for tx, ty in steps:
        nx, ny = i + tx, j + ty
        if (
            nx in range(N)
            and ny in range(N)
            and not visited[nx][ny]
            and garage[round][nx][ny] == target
        ):
            visited[nx][ny] = True
            dfs(round, visited, nx, ny, target)


def cal_score():
    min_x = min(i for i, j in neighbors)
    max_x = max(i for i, j in neighbors)
    min_y = min(j for i, j in neighbors)
    max_y = max(j for i, j in neighbors)
    return len(neighbors) + (max_x - min_x + 1) * (max_y - min_y + 1)


def set_next_board(round):
    next = [row[:] for row in garage[round]]
    for i, j in neighbors:
        next[i][j] = 0
    garage[round + 1] = [[c for c in row if c != 0] for row in next]


def calculateNeighbor(rnd):
    hasNeighbor = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N - 1):
        for y in range(N):
            if garage[rnd][x][y] == garage[rnd][x + 1][y]:
                hasNeighbor[x][y] = hasNeighbor[x + 1][y] = 1
    for x in range(N):
        for y in range(N - 1):
            if garage[rnd][x][y] == garage[rnd][x][y + 1]:
                hasNeighbor[x][y] = hasNeighbor[x][y + 1] = 1
    return hasNeighbor


def simul(round, score):
    if round == 3:
        global answer
        answer = max(answer, score)
        return

    if round == 2:
        hasNeighbor = calculateNeighbor(round)

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if round == 2 and hasNeighbor[i][j] == 0:
                    get_score = 2
                else:
                    global neighbors
                    neighbors = []
                    dfs(round, visited, i, j, garage[round][i][j])
                    get_score = cal_score()
                if round < 2:
                    set_next_board(round)
                simul(round + 1, score + get_score)


def sol():
    colors.reverse()
    garage[0] = [list(row) for row in zip(*colors)]

    simul(0, 0)
    print(answer)


sol()
