from collections import deque

N = int(input())
K = int(input())
apples = [map(int, input().split()) for _ in range(K)]
L = int(input())
moves = [input().split() for _ in range(L)]


def change_direction(current, cmd):
    tx, ty = current
    if cmd == "L":
        if tx == 0 and ty == 1:
            return (-1, 0)
        if tx == -1 and ty == 0:
            return (0, -1)
        if tx == 0 and ty == -1:
            return (1, 0)
        if tx == 1 and ty == 0:
            return (0, 1)
    elif cmd == "D":
        if tx == 0 and ty == 1:
            return (1, 0)
        if tx == 1 and ty == 0:
            return (0, -1)
        if tx == 0 and ty == -1:
            return (-1, 0)
        if tx == -1 and ty == 0:
            return (0, 1)


def sol():
    board = [
        [
            0 if i != 0 and i != N + 1 and j != 0 and j != N + 1 else -1
            for i in range(N + 2)
        ]
        for j in range(N + 2)
    ]
    board[1][1] = 1
    for x, y in apples:
        board[x][y] = 2

    snake = deque([(1, 1)])

    direction = (0, 1)
    time = 0

    for X, L in moves:
        for _ in range(time, int(X)):
            time += 1
            cx, cy = snake[0]
            nx, ny = cx + direction[0], cy + direction[1]
            if board[nx][ny] == -1 or board[nx][ny] == 1:
                print(time)
                return
            snake.appendleft((nx, ny))
            if board[nx][ny] != 2:
                x, y = snake.pop()
                board[x][y] = 0
            board[nx][ny] = 1
        direction = change_direction(direction, L)

    while True:
        time += 1
        cx, cy = snake[0]
        nx, ny = cx + direction[0], cy + direction[1]
        if board[nx][ny] == -1 or board[nx][ny] == 1:
            print(time)
            return
        snake.appendleft((nx, ny))
        if board[nx][ny] != 2:
            x, y = snake.pop()
            board[x][y] = 0
        board[nx][ny] = 1


sol()
