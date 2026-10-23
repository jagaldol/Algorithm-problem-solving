from math import ceil

def solution(progresses, speeds):
    days = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    
    answer = []
    left = 0
    
    while left < len(days):
        right = left + 1
        
        while right < len(days) and days[right] <= days[left]:
            right += 1
        
        answer.append(right - left)
        left = right
    return answer
