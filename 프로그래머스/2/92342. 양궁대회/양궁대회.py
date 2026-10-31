def solution(n, info):
    
    def get_diff(targets):
        lion_score = 0
        apeach_score = 0
        for idx, (target, apeach) in enumerate(zip(targets, info)):
            score = 10 - idx
            if target:
                lion_score += score
            elif apeach > 0:
                apeach_score += score
                
        return lion_score - apeach_score
    
    answer = [-1]
    top = 0
    for mask in range(1 << 11):
        targets = [bool(mask & 1 << bit) for bit in range(9, -1, -1)] + [False]
        diff = get_diff(targets)
        if diff <= 0:
            continue
        
        result = [0] * 11
        for idx, target in enumerate(targets):
            if not target:
                continue
            result[idx] = info[idx] + 1
        used = sum(result)
        if used > n:
            continue
            
        result[10] = n - used
        
        if diff > top or (diff == top and result[::-1] > answer[::-1]):
            top = diff
            answer = result
        

    
    return answer