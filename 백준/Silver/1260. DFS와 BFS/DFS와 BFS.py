def DFS_recur(adj, visited, N, V):
    visited[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if adj[V][i] == 1 and visited[i] == 0:
            DFS_recur(adj, visited, N, i)

def DFS(adj, N, V):
    visited = [0 for _ in range(N + 1)]

    DFS_recur(adj, visited, N, V)
    print()

def BFS(adj, N, V):
    visited = [0 for _ in range(N + 1)]

    queue = [V]

    while len(queue) > 0:
        now = queue.pop(0)
        if visited[now] == 1:
            continue
        visited[now] = 1
        print(now, end=' ')
        for i in range(1, N + 1):
            if adj[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                
    print()

N, M, V = map(int, input().split())

adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())

    adj[v1][v2] = 1
    adj[v2][v1] = 1

DFS(adj, N, V)

BFS(adj, N, V)