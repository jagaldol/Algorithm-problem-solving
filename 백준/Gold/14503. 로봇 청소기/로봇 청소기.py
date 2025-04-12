import sys

input = sys.stdin.readline

N, M = map(int, input().split())

steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sol():
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    while True:
        if board[r][c] == 0:
            answer += 1
            board[r][c] = -1
        if any(board[r + dx][c + dy] == 0 for dx, dy in steps if r + dx in range(N) and c + dy in range(M)):
            d = (d - 1) % 4
            dx, dy = steps[d]
            nr, nc = r + dx, c + dy
            if nr in range(N) and nc in range(M) and board[nr][nc] == 0:
                r, c = nr, nc
        else:
            dx, dy = steps[d]
            nr, nc = r - dx, c - dy
            if nr in range(N) and nc in range(M) and board[nr][nc] != 1:
                r, c = nr, nc
                continue
            else:
                break

    print(answer)


sol()
