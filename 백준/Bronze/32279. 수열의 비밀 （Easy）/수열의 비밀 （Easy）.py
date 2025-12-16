n = int(input())
p, q, r, s = map(int, input().split())
A = [0 for _ in range(n + 1)]
A[1] = int(input())

for i in range(2, n + 1):
    if i % 2 == 0:
        A[i] = p * A[i // 2] + q
    else:
        A[i] = r * A[i // 2] + s

print(sum(A))
