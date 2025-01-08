import sys
from collections import deque

input = sys.stdin.readline
K = int(input())


def sol():
    stack = deque()
    for _ in range(K):
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)
    print(sum(stack))


sol()
