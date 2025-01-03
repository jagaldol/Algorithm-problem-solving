import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
result = 0


def get_tornado_effect(direction):
    """
    이동 방향에 따른 영향을 리턴

    tornado[2][2] 지점이 중앙 지점
    """
    tornado = [
        [0.00, 0.00, 0.02, 0.00, 0.00],
        [0.00, 0.10, 0.07, 0.01, 0.00],
        [0.05, 0.00, 0.00, 0.00, 0.00],
        [0.00, 0.10, 0.07, 0.01, 0.00],
        [0.00, 0.00, 0.02, 0.00, 0.00],
    ]
    if direction == 1:
        return [[tornado[j][4 - i] for j in range(5)] for i in range(5)]
    if direction == 2:
        return [[tornado[4 - i][4 - j] for j in range(5)] for i in range(5)]
    if direction == 3:
        return [[tornado[4 - j][i] for j in range(5)] for i in range(5)]

    return tornado


def tornado_effect(x, y, direction):
    tornado = get_tornado_effect(direction)

    moved = 0
    global result
    for i in range(5):
        for j in range(5):
            nx = x - 2 + i
            ny = y - 2 + j
            sand = int(tornado[i][j] * board[x][y])
            moved += sand
            if nx in range(N) and ny in range(N):
                board[nx][ny] += sand
            else:
                result += sand
    tx, ty = directions[direction]
    nx, ny = x + tx, y + ty
    sand = board[x][y] - moved
    if nx in range(N) and ny in range(N):
        board[nx][ny] += sand
    else:
        result += sand
    board[x][y] = 0


def find_next_direction(visited, x, y, d):
    for nd in range(4):
        if (d + nd) % 2 == 0:
            continue
        tx, ty = directions[nd]
        nx, ny = x + tx, y + ty
        if nx in range(N) and ny in range(N) and visited[nx][ny]:
            return d

    for nd in range(4):
        tx, ty = directions[nd]
        nx, ny = x + tx, y + ty
        if nx in range(N) and ny in range(N) and not visited[nx][ny]:
            for tx2, ty2 in directions:
                if tx + tx2 == 0 and ty + ty2 == 0:
                    continue
                nx2, ny2 = nx + tx2, ny + ty2
                if nx2 in range(N) and ny2 in range(N) and visited[nx2][ny2]:
                    return nd


def spell_tornado():
    visited = [[False for _ in range(N)] for _ in range(N)]
    start, end = N // 2, N // 2
    visited[start][end] = True

    d = 0
    tx, ty = directions[d]
    x, y = start + tx, end + ty

    visited[x][y] = True
    tornado_effect(x, y, d)

    d = 1
    while True:
        tx, ty = directions[d]
        x, y = x + tx, y + ty

        visited[x][y] = True
        tornado_effect(x, y, d)

        if x == 0 and y == 0:
            print(result)
            break
        d = find_next_direction(visited, x, y, d)


spell_tornado()
