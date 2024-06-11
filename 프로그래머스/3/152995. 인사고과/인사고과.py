def solution(scores):
    failed = [False for _ in scores]
    scores = [(idx, score) for idx, score in enumerate(scores)]
    
    sorted_scores = sorted(scores, key=lambda x: (-x[1][0], x[1][1]))
    
    max_value = sorted_scores[0][1][1]
    
    for idx, score in sorted_scores:
        if score[1] < max_value:
            failed[idx] = True
        else:
            max_value = score[1]
    
    if failed[0]:
        return -1
    
    my_score = sum(scores[0][1])
    
    return sum([1 for idx, score in scores if not failed[idx] and sum(score) > my_score]) + 1