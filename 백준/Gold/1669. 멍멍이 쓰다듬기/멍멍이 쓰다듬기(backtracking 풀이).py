import sys
from collections import deque


def sol():
    input = sys.stdin.readline

    X, Y = map(int, input().split())

    stack = deque()

    stack.append((X + 1, 1, 1))

    if X == Y:
        print(0)
        return

    while len(stack) > 0:
        height, now, count = stack.pop()

        sum_to_one = now * (now - 1) // 2

        if height + sum_to_one == Y:
            print(count + now - 1)
            break
        elif height + sum_to_one < Y:
            nexts = (now - 1, now, now + 1)
            for next in nexts:
                if next >= 0:
                    stack.append((height + next, next, count + 1))


sol()
