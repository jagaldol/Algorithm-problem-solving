import sys


def sol():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    board = []
    for i in range(n):
        line = list(map(int, list(input().rstrip())))
        board.append(line)

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    high = max(map(max, board))

    print(high**2)


sol()
