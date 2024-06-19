def solution(num_list):
    answer = num_list[:]
    if answer[-1] > answer[-2]:
        answer.append(answer[-1] - answer[-2])
    else:
        answer.append(answer[-1] * 2)
    return answer