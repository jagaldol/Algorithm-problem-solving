import sys
from collections import deque

input = sys.stdin.readline
n = int(input())


def sol():
    stack = deque()

    pushed = 0
    result = []
    for _ in range(n):
        num = int(input())

        if pushed < num:
            stack.extendleft([i for i in range(pushed + 1, num)])
            result.extend(["+"] * (num - pushed) + ["-"])
            pushed = num
        elif not stack:
            print("NO")
            return
        elif stack[0] == num:
            stack.popleft()
            result.append("-")
        else:
            print("NO")
            return
    print("\n".join(result))


sol()
