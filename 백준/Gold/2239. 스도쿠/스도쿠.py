import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(9)]


def valid_num(x, y):
    num = set(range(1, 10))
    rs = x // 3
    cs = y // 3
    for i in range(9):
        if board[x][i] in num:
            num.remove(board[x][i])
        if board[i][y] in num:
            num.remove(board[i][y])
        ri = rs * 3 + i // 3
        ci = cs * 3 + i % 3
        if board[ri][ci] in num:
            num.remove(board[ri][ci])

    return list(num)


def backtrack(blanks, step):
    if step == len(blanks):
        return True

    x, y = blanks[step]
    for n in valid_num(x, y):
        board[x][y] = n
        if backtrack(blanks, step + 1):
            return True
        board[x][y] = 0

    return False


def sol():
    blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    backtrack(blanks, 0)

    for i in range(9):
        print("".join(map(str, board[i])))


sol()
