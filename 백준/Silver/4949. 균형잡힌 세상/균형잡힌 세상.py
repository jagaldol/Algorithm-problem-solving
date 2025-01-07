import sys
from collections import deque

input = sys.stdin.readline


def check_balance(sentence):
    stack = deque()
    for s in sentence:
        if s == "(":
            stack.append(s)
        elif s == "[":
            stack.append(s)
        elif s == ")":
            if not stack or stack.pop() != "(":
                return False
        elif s == "]":
            if not stack or stack.pop() != "[":
                return False
    if stack:
        return False
    return True


def sol():
    while (sentence := input().rstrip()) != ".":
        print("yes" if check_balance(sentence) else "no")


sol()
