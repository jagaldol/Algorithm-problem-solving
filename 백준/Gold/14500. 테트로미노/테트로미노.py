import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(path):
    if len(path) == 4:
        global answer
        answer = max(answer, sum(board[i][j] for i, j in path))
        return
    for x, y in path:
        for tx, ty in steps:
            nx, ny = x + tx, y + ty
            if nx in range(N) and ny in range(M) and not visited[nx][ny]:
                visited[nx][ny] = True
                path.append((nx, ny))
                dfs(path)
                path.pop()
                visited[nx][ny] = False


def sol():
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs([(i, j)])

    print(answer)


sol()
