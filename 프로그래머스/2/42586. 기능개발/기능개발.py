from math import ceil

def solution(progresses, speeds):
    deploy_days = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    
    now = 0
    answer = []
    
    for day in deploy_days:
        if day > now:
            now = day
            answer.append(1)
        else:
            answer[-1] += 1
    return answer
