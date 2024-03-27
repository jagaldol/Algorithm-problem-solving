answer = []


def hanoi(n, s, e):
    if n == 1:
        answer.append([s, e])
        return
    empty_place = [i for i in [1, 2, 3] if not i in [s, e]][0]
    hanoi(n - 1, s, empty_place)
    answer.append([s, e])
    hanoi(n - 1, empty_place, e)


def solution(n):
    hanoi(n, 1, 3)
    return answer
