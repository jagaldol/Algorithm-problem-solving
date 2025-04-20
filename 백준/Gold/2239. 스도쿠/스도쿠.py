import sys

input = sys.stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(9)]


def get_invalid_numbers(x, y):
    nums = set()
    rs = x // 3
    cs = y // 3
    for i in range(9):
        nums.add(board[x][i])
        nums.add(board[i][y])
        nums.add(board[rs * 3 + i // 3][cs * 3 + i % 3])

    return list(nums)


def backtrack(blanks, step):
    if step == len(blanks):
        return True

    x, y = blanks[step]
    invalid_nums = get_invalid_numbers(x, y)

    for i in range(1, 10):
        if i in invalid_nums:
            continue
        board[x][y] = i
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
