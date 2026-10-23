from collections import Counter

def solution(participant, completion):
    counter = Counter(participant)
    for name in completion:
        counter[name] -= 1
    
    for name, left in counter.items():
        if left > 0:
            return name
    return ""