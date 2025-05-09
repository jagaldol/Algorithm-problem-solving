import math

N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())

lens = [len(num) for num in nums]
mods = [int(num) % K for num in nums]

# pow10_mod[i] = 10^len(nums[i]) % K
pow10_mod = [1] * 51
for i in range(1, 51):
    pow10_mod[i] = (pow10_mod[i - 1] * 10) % K

# dp[mask][mod]: mask 상태에서 mod 나머지로 끝나는 경우의 수
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for mask in range(1 << N):
    for mod in range(K):
        if dp[mask][mod] == 0:
            continue
        for i in range(N):
            if not (mask & (1 << i)):
                next_mask = mask | (1 << i)
                next_mod = (mod * pow10_mod[lens[i]] + mods[i]) % K
                dp[next_mask][next_mod] += dp[mask][mod]

total = dp[(1 << N) - 1][0]
denom = math.factorial(N)

# 약분
g = math.gcd(total, denom)
print(f"{total // g}/{denom // g}")
