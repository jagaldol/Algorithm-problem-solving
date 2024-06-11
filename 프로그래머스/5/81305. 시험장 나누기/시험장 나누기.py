import sys
sys.setrecursionlimit(10 ** 6)

p = [-1] * 10000
l = [-1] * 10000
r = [-1] * 10000
root = -1
cnt = 0


def dfs(num, cur, limit):
    global cnt
    
    lv = 0 if l[cur] == -1 else dfs(num, l[cur], limit)
    rv = 0 if r[cur] == -1 else dfs(num, r[cur], limit)
    
    if num[cur] + lv + rv <= limit:
        return num[cur] + lv + rv
    
    if num[cur] + min(lv, rv) <= limit:
        cnt += 1
        return num[cur] + min(lv, rv)
    
    cnt += 2
    return num[cur]
    

def solution(k, num, links):
    global root
    
    
    for idx, (left, right) in enumerate(links):
        if left != -1:
            l[idx] = left
            p[left] = idx
        if right != -1:
            r[idx] = right
            p[right] = idx
            
    root = sum([i for i in range(len(num)) if p[i] == -1])
    
    st = max(num)
    en = 10 ** 4 * len(num)
    
    while st < en:
        mid = (st + en) // 2
        global cnt
        cnt = 0
        
        dfs(num, root, mid)
        
        if cnt + 1 <= k:
            en = mid
        else:
            st = mid + 1
        
    return st