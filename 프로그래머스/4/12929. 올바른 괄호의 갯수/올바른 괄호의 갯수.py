cnt = 0

def dfs(l, r):
    global cnt
    if l == 0 and r == 0: cnt += 1
    if r > 0:
        dfs(l, r - 1)
    if l > 0:
        dfs(l-1, r+1)

def solution(n):
    dfs(n, 0)
    return cnt