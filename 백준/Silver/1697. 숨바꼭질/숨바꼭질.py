from collections import deque

N, K = map(int, input().split())


def sol():
    queue = deque([(N, 0)])
    visited = [False for _ in range(100_001)]
    while True:
        x, t = queue.popleft()
        if x == K:
            print(t)
            break
        visited[x] = True
        nxs = [2 * x, x + 1, x - 1]
        for nx in nxs:
            if nx in range(100_001) and not visited[nx]:
                queue.append((nx, t + 1))


sol()
