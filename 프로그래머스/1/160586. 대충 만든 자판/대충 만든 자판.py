import string

def solution(keymap, targets):
    
    cost = dict([[alphabet, 101] for alphabet in string.ascii_uppercase])
    for key in keymap:
        for idx, alphabet in enumerate(key):
            cost[alphabet] = min(cost[alphabet], idx + 1)
        
    answer = []
    
    for target in targets:
        need = 0
        for alphabet in target:
            need += cost[alphabet]
            if cost[alphabet] == 101:
                need = -1
                break
        answer.append(need)
    return answer