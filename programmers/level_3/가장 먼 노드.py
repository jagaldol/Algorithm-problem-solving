from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [False] * (n + 1)
    queue = deque()

    queue.append((1, 0))
    visited[1] = True

    answer = 0
    longest = 0

    while len(queue) > 0:
        current, distance = queue.popleft()
        if longest < distance:
            answer = 0
            longest = distance

        answer += 1

        visited[current] = True

        for next in graph[current]:
            if visited[next]:
                continue

            visited[next] = True
            queue.append((next, distance + 1))

    return answer
