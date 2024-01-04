import sys
from collections import deque


def is_bipartite(adj, V):
    classification = [0 for _ in range(V + 1)]

    stack = deque()

    for i in range(1, V + 1):
        if classification[i] != 0:
            continue
        classification[i] = 1
        stack.append(i)

        while not len(stack) == 0:
            now = stack.pop()
            next_location = 2 if classification[now] == 1 else 1

            for next_node in adj[now]:
                if classification[next_node] == 0:
                    classification[next_node] = next_location
                    stack.append(next_node)
                elif classification[next_node] != next_location:
                    print("NO")
                    return

    print("YES")


def sol():
    input = sys.stdin.readline
    K = int(input())

    for i in range(K):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V + 1)]
        for j in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        is_bipartite(adj, V)


sol()
