def solution(mats, park):
    best = -1
    n = len(park)
    m = len(park[0])
    
    def check(mat, x, y):
        for i in range(mat):
            for j in range(mat):
                nx = x + i
                ny = y + j
                if nx >= n or ny >= m or park[nx][ny] != "-1":
                    return False
        return True
    
    for i in range(n):
        for j in range(m):
            for mat in mats:
                if check(mat, i, j):
                    best = max(best, mat)
                
    return best