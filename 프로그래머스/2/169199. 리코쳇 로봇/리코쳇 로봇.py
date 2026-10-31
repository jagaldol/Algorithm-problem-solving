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
        
        for dx, dy in steps:
            distance = 1
            while True:
                nx = x + dx * distance
                ny = y + dy * distance
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if board[nx][ny] == 'D':
                    break
                distance += 1
            distance -= 1
            nx = x + dx * distance
            ny = y + dy * distance
            if costs[x][y] + 1 < costs[nx][ny]:
                queue.append((nx, ny))
                costs[nx][ny] = costs[x][y] + 1
                
    gx, gy = next((i, j) for i in range(n) for j in range(m) if board[i][j] == 'G')

    if costs[gx][gy] == float('inf'):
        return -1
    return costs[gx][gy]