from collections import deque


def bfs(relation, N, start):
    que = deque()
    visited = [False] * (N + 1)

    que.appendleft([start, 0])
    visited[start] = True

    total = 0

    while len(que) > 0:
        now, step = que.pop()

        total += step

        for i in range(1, N + 1):
            if not visited[i] and relation[now][i]:
                que.appendleft([i, step + 1])
                visited[i] = True

    return total


def sol():
    N, M = map(int, input().split())
    relation = [[False] * (N + 1) for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        relation[a][b] = True
        relation[b][a] = True

    lowest = 999999999
    result = 0
    for i in range(1, N + 1):
        total = bfs(relation, N, i)
        if total < lowest:
            lowest = total
            result = i

    print(result)


sol()
