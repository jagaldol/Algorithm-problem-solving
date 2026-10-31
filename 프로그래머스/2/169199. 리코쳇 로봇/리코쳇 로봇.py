from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    costs = [[float('inf') for _ in range(m)] for _ in range(n)]
    
    sx, sy = next((i, j) for i in range(n) for j in range(m) if board[i][j] == 'R')
    queue = deque([(sx, sy)])
    costs[sx][sy] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if board[x][y] == 'G':
            return costs[x][y]
        
        for dx, dy in steps:
            nx, ny = x, y
            while True:
                tx, ty = nx + dx, ny + dy
                if not (0 <= tx < n and 0 <= ty < m):
                    break
                if board[tx][ty] == 'D':
                    break
                nx, ny = tx, ty
    
            if costs[x][y] + 1 < costs[nx][ny]:
                queue.append((nx, ny))
                costs[nx][ny] = costs[x][y] + 1
                
    return -1