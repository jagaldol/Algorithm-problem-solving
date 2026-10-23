from collections import Counter

def solution(participant, completion):
    remain = Counter(participant) - Counter(completion)
    return list(remain)[0]