from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for ordered_dungeons in permutations(dungeons):
        energy = k
        cnt = 0
        for need, cost in ordered_dungeons:
            if energy < need:
                continue
            energy -= cost
            cnt += 1
        answer = max(answer, cnt)
    return answer