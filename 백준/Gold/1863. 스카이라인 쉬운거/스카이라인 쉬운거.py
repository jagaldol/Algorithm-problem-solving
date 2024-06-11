import sys
from collections import deque


def sol():
    input = sys.stdin.readline

    n = int(input())
    skylines = [list(map(int, input().split())) for _ in range(n)]

    stack = deque()

    building_num = 0

    for x, y in skylines:
        while len(stack) > 0:
            if y > stack[-1]:
                stack.append(y)
                break
            elif y == stack[-1]:
                break
            else:
                stack.pop()
                building_num += 1
        if len(stack) == 0 and y != 0:
            stack.append(y)

    print(building_num + len(stack))


sol()
