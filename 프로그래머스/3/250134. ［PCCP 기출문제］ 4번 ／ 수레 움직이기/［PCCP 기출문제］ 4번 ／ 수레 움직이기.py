def solution(maze):
    n, m = len(maze), len(maze[0])
    red_visited = [[False for _ in range(m)] for _ in range(n)]
    blue_visited = [[False for _ in range(m)] for _ in range(n)]
    steps = [(-1, 0), (0 , -1), (1, 0), (0, 1), (0, 0)]
    
    answer = 0
    
    def dfs(rx, ry, bx, by):
        answer = float('inf')
        
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            return 0
        
        if maze[rx][ry] == 3:
            nrx, nry = rx, ry
            for dbx, dby in steps:
                nbx, nby = bx + dbx, by + dby
                if not (0 <= nbx < n and 0 <= nby < m) or blue_visited[nbx][nby] or maze[nbx][nby] == 5:
                    continue
                if (nrx, nry) == (nbx, nby):
                    continue
                blue_visited[nbx][nby] = True
                answer = min(answer, dfs(nrx, nry, nbx, nby) + 1)
                blue_visited[nbx][nby] = False
        elif maze[bx][by] == 4:
            nbx, nby = bx, by
            for drx, dry in steps:
                nrx, nry = rx + drx, ry + dry
                if not (0 <= nrx < n and 0 <= nry < m) or red_visited[nrx][nry] or maze[nrx][nry] == 5:
                    continue
                if (nrx, nry) == (nbx, nby):
                    continue
                red_visited[nrx][nry] = True
                answer = min(answer, dfs(nrx, nry, nbx, nby) + 1)
                red_visited[nrx][nry] = False
            
        else:
            for drx, dry in steps:
                nrx, nry = rx + drx, ry + dry
                if not (0 <= nrx < n and 0 <= nry < m) or red_visited[nrx][nry] or maze[nrx][nry] == 5:
                    continue

                for dbx, dby in steps:
                    nbx, nby = bx + dbx, by + dby
                    if not (0 <= nbx < n and 0 <= nby < m) or blue_visited[nbx][nby] or maze[nbx][nby] == 5:
                        continue
                    if (nrx, nry) == (nbx, nby):
                        continue
                    if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                        continue
                    red_visited[nrx][nry] = True
                    blue_visited[nbx][nby] = True
                    answer = min(answer, dfs(nrx, nry, nbx, nby) + 1)
                    red_visited[nrx][nry] = False
                    blue_visited[nbx][nby] = False
        return answer
    
    rx, ry = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 1)
    bx, by = next((i, j) for i in range(n) for j in range(m) if maze[i][j] == 2)
    
    red_visited[rx][ry] = True
    blue_visited[bx][by] = True
    
    answer = dfs(rx, ry, bx, by)
    return 0 if answer == float('inf') else answer