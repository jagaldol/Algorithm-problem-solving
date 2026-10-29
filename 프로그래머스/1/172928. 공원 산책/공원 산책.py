def solution(park, routes):
    n, m = len(park), len(park[0])
    ops = {
        "N": (-1 ,0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }
    
    x, y = next((i, j) for i in range(n) for j in range(m) if park[i][j] == "S")
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        dx, dy = ops[direction]
        nx, ny = x + distance * dx, y + distance * dy
        
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if any(park[x + dx * k][y + dy * k] == "X" for k in range(1, distance + 1)):
            continue
        x, y = nx, ny
    
    return [x, y]
