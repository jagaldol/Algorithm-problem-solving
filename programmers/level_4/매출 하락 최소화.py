import sys

sys.setrecursionlimit(10**6)

s = []
children = []


def min_loss(current, leader=False):
    length = len(children[current])
    if length == 0:
        return s[current], 0

    children_min = [min_loss(child) for child in children[current]]

    case1 = s[current] + sum(min(child_min) for child_min in children_min)
    case2 = min(
        [
            sum(
                [
                    children_min[i][0] if i == j else min(children_min[i])
                    for i in range(length)
                ]
            )
            for j in range(length)
        ]
    )

    return case1, case2


def solution(sales, links):
    global s, children
    s = sales
    children = [[] for _ in sales]
    for a, b in links:
        children[a - 1].append(b - 1)

    return min(min_loss(0))
