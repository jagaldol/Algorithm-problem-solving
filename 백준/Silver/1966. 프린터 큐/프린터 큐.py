import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def sol():
    for _ in range(T):
        N, M = map(int, input().split())
        priorities = list(map(int, input().split()))
        queue = deque(enumerate(priorities))
        while queue:
            idx, current = queue.popleft()
            if queue and current < max(p for i, p in queue):
                queue.append((idx, current))
            elif idx == M:
                print(N - len(queue))
                break


sol()
