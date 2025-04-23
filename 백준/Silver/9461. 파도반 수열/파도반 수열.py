import sys

input = sys.stdin.readline

T = int(input())

P = [1, 1, 1, 2, 2] + [0] * 95

for i in range(5, 100):
    P[i] = P[i - 1] + P[i - 5]

for _ in range(T):
    N = int(input())
    print(P[N - 1])
