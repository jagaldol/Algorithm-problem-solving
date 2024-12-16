import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

T = int(input())
board = []
visited = []
steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
M = 0
N = 0
K = 0


def dfs(x, y):
    visited[x][y] = True

    for tx, ty in steps:
        nx, ny = x + tx, y + ty
        if nx in range(N) and ny in range(M) and not visited[nx][ny] and board[nx][ny]:
            dfs(nx, ny)


def sol():
    for _ in range(T):
        global M, N, K, board, visited

        M, N, K = map(int, input().split())
        positions = [list(map(int, input().split())) for _ in range(K)]
        board = [[False for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]
        for x, y in positions:
            board[y][x] = True

        answer = 0
        for x, y in positions:
            if not visited[y][x]:
                dfs(y, x)
                answer += 1

        print(answer)


sol()
