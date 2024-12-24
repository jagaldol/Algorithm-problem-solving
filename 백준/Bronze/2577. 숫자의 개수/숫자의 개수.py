from collections import Counter

A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)

counter = Counter(res)
for i in range(10):
    print(counter[str(i)])
