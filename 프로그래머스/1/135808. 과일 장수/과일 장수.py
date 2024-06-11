def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    answer = 0
    for i in range(m - 1, len(sorted_score), m):
        answer += sorted_score[i] * m
        
    return answer