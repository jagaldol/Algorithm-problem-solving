import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    selections = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    cycle_num = 0

    for i in range(1, n + 1):
        cycle = []
        node = i
        while not visited[node]:
            visited[node] = True
            cycle.append(node)
            node = selections[node]

        if node in cycle:
            cycle_num += len(cycle) - cycle.index(node)

    print(n - cycle_num)
