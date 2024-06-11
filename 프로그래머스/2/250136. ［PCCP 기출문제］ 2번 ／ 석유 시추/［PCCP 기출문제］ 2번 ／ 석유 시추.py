from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

visited = []
expected = []

moves = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)

def dfs(land, x, y, path, start):
    if land[x][y] == 0:
        return
    
    path.append((x, y))
    
    for tx, ty in moves:
        nx, ny = x + tx, y + ty
        if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and not visited[nx][ny]:
            visited[x + tx][y + ty] = True
            dfs(land, x + tx, y + ty, path, False)
    
    if start:
        for k in set([j for i, j in path]):
            expected[k] += len(path)
    

def solution(land):
    global visited, expected
    visited = [[False] * len(land[0]) for _ in land]
    expected = [0] * len(land[0])
    
    for i, _ in enumerate(land):
        for j, _ in enumerate(land[0]):
            if not visited[i][j]:
                visited[i][j] = True
                dfs(land, i, j, [], True)
    return max(expected)
