from math import ceil

def solution(progresses, speeds):
    remain = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    cnt = 1
    now = remain[0]
    answer = []
    
    for day in remain[1:]:
        if day > now:
            answer.append(cnt)
            cnt = 1
            now = day
        else:
            cnt += 1
    answer.append(cnt)
    return answer
