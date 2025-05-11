import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

index = 0
stack = []
indices = [0] * (V + 1)
lowlink = [0] * (V + 1)
on_stack = [False] * (V + 1)
SCCs = []
id_counter = 1


def tarjan(v):
    global index, id_counter
    indices[v] = lowlink[v] = id_counter
    id_counter += 1
    stack.append(v)
    on_stack[v] = True

    for w in graph[v]:
        if indices[w] == 0:
            tarjan(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif on_stack[w]:
            lowlink[v] = min(lowlink[v], indices[w])

    if lowlink[v] == indices[v]:
        scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)
            if w == v:
                break
        SCCs.append(sorted(scc))


for v in range(1, V + 1):
    if indices[v] == 0:
        tarjan(v)

SCCs.sort(key=lambda x: x[0])

print(len(SCCs))
for scc in SCCs:
    print(*scc, -1)
