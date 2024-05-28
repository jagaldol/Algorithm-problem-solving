import sys
import itertools

sys.setrecursionlimit(10**7)

is_sheep = []
tree = []
answer = 0


def dfs(sheep, wolf, current, around):
    if is_sheep[current]:
        sheep += 1
        global answer
        answer = max(answer, sheep)
    else:
        wolf += 1
    if wolf >= sheep:
        return

    around.extend(tree[current])
    for node in around:
        dfs(sheep, wolf, node, [i for i in around if i != node])


def solution(info, edges):
    global tree, is_sheep
    tree = [[] for _ in info]
    is_sheep = [i == 0 for i in info]

    for a, b in edges:
        tree[a].append(b)

    dfs(0, 0, 0, [])
    return answer