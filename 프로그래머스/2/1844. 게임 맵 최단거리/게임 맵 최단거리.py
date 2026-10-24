from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0])
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    visited = [row[:] for row in maps]
    visited[0][0] = 2
    
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, distance = queue.popleft()
        if x == m - 1 and y == n - 1:
            return distance
        
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 1:
                visited[nx][ny] = 2
                queue.append((nx, ny, distance + 1))
        
    
    return -1