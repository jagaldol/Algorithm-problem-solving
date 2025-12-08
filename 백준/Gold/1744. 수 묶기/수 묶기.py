import sys

input = sys.stdin.readline

N = int(input())
neg = []
pos = []
zeros = 0
for _ in range(N):
    a = int(input())
    if a < 0:
        neg.append(a)
    elif a > 0:
        pos.append(a)
    else:
        zeros += 1

neg.sort()
pos.sort(reverse=True)

answer = 0

idx = 0
while idx < len(neg) - 1:
    answer += neg[idx] * neg[idx + 1]
    idx += 2

if idx == len(neg) - 1 and zeros == 0:
    answer += neg[idx]

idx = 0
while idx < len(pos) - 1:
    if pos[idx] == 1 or pos[idx + 1] == 1:
        answer += pos[idx] + pos[idx + 1]
    else:
        answer += pos[idx] * pos[idx + 1]
    idx += 2

if idx == len(pos) - 1:
    answer += pos[idx]

print(answer)
