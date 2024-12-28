import sys

input = sys.stdin.readline

N = int(input())
num_counts = [0 for _ in range(10001)]
for _ in range(N):
    num = int(input())
    num_counts[num] += 1

for i in range(1, 10001):
    count = num_counts[i]
    for _ in range(count):
        print(i)
