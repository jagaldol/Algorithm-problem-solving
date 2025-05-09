MOD = 10**9 + 7

N = int(input())
S = list(map(int, input().split()))
S.sort()

pow2 = [1] * N
for i in range(1, N):
    pow2[i] = (pow2[i - 1] * 2) % MOD

answer = 0
for i in range(N):
    max_count = pow2[i]
    min_count = pow2[N - 1 - i]
    answer = (answer + S[i] * (max_count - min_count)) % MOD

print(answer)
