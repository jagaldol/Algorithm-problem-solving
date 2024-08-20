import bisect


def solution(operations):
    container = []

    for operation in operations:
        op, number = operation.split()
        if op == "I":
            bisect.insort(container, int(number))
        else:
            if len(container) == 0:
                continue
            if number == "1":
                container.pop()
            else:
                container.pop(0)

    answer = [max(container), min(container)] if len(container) > 0 else [0, 0]
    return answer
