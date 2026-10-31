def solution(maze):
    n, m = len(maze), len(maze[0])
    red_visited = [[False for _ in range(m)] for _ in range(n)]
    blue_visited = [[False for _ in range(m)] for _ in range(n)]
    steps = [(-1, 0), (0 , -1), (1, 0), (0, 1)]
    
    rx, ry = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 1)
    bx, by = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 2)
    rgx, rgy = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 3)
    bgx, bgy = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 4)
    
    red_visited[rx][ry] = True
    blue_visited[bx][by] = True
    
    def next_positions(x, y, goal, visited):
        if maze[x][y] == goal:
            return[(x, y)]
        
        result = []
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] or maze[nx][ny] == 5:
                continue
            
            result.append((nx, ny))
        return result        
    
    
    best = float('inf')
    
    def dfs(rx, ry, bx, by, turns):
        nonlocal best
        
        remaining = max(
            abs(rx - rgx) + abs(ry - rgy),
            abs(bx - bgx) + abs(by - bgy),
        )
        
        if turns + remaining >= best:
            return
        
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            best = turns
            return
        
        red_moves = next_positions(rx, ry, 3, red_visited)
        blue_moves = next_positions(bx, by, 4, blue_visited)
        
        for nrx, nry in red_moves:
            for nbx, nby in blue_moves:
                if (nrx, nry) == (nbx, nby):
                    continue
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue
                
                red_before = red_visited[nrx][nry]
                blue_before = blue_visited[nbx][nby]
                
                red_visited[nrx][nry] = True
                blue_visited[nbx][nby] = True
                dfs(nrx, nry, nbx, nby, turns + 1)
                red_visited[nrx][nry] = red_before
                blue_visited[nbx][nby] = blue_before
    
    dfs(rx, ry, bx, by, 0)
    
    return 0 if best == float('inf') else best