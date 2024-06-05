N = int(input())
max_value = 0


def move_left(origin_board):
    board = [[v for v in row] for row in origin_board]
    for i in range(N):
        k = 0
        for j in range(N):
            if board[i][j] != 0:
                board[i][k] = board[i][j]
                k += 1
        for l in range(k, N):
            board[i][l] = 0

    for i in range(N):
        for j in range(N - 1):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                for k in range(j + 1, N - 1):
                    board[i][k] = board[i][k + 1]
                board[i][N - 1] = 0
    return board


def v_flip(board):
    return [[board[i][N - 1 - j] for j in range(N)] for i in range(N)]


def turn_left(board):
    return [[board[j][N - 1 - i] for j in range(N)] for i in range(N)]


def turn_right(board):
    return [[board[N - 1 - j][i] for j in range(N)] for i in range(N)]


def dfs(board, step):
    if step == 5:
        global max_value
        max_value = max(max_value, max(v for row in board for v in row))
        return

    new_board = move_left(board)
    dfs(new_board, step + 1)

    new_board = move_left(v_flip(board))
    dfs(v_flip(new_board), step + 1)

    new_board = move_left(turn_left(board))
    dfs(turn_right(new_board), step + 1)

    new_board = move_left(turn_right(board))
    dfs(turn_left(new_board), step + 1)


def sol():
    board = [list(map(int, input().split())) for _ in range(N)]
    dfs(board, 0)
    print(max_value)


sol()
