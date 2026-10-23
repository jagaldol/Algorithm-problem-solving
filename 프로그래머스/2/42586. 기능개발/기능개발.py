def solution(progresses, speeds):
    remain = [(100 - progress + speed - 1) // speed for progress, speed in zip(progresses, speeds)]
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
