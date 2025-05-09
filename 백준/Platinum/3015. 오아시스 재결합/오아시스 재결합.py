import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = 0

for _ in range(n):
    h = int(input())
    count = 1

    while stack and stack[-1][0] <= h:
        top_height, top_count = stack.pop()
        answer += top_count
        if top_height == h:
            count += top_count

    if stack:
        answer += 1

    stack.append((h, count))

print(answer)
