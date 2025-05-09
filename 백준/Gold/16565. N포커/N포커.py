MOD = 10**4 + 7

N = int(input())

MAX = 52
factorial = [1] * (MAX + 1)
inverse_factorial = [1] * (MAX + 1)


for i in range(1, MAX + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD


def mod_inverse(x):
    return pow(x, MOD - 2, MOD)


inverse_factorial[MAX] = mod_inverse(factorial[MAX])

for i in range(MAX - 1, -1, -1):
    inverse_factorial[i] = (inverse_factorial[i + 1] * (i + 1)) % MOD


def comb(a, b):
    if b < 0 or b > a:
        return 0
    return factorial[a] * inverse_factorial[b] % MOD * inverse_factorial[a - b] % MOD


result = 0
for i in range(1, 14):
    sign = 1 if i % 2 == 1 else -1
    num_choose = comb(13, i)
    rest_choose = comb(52 - 4 * i, N - 4 * i)
    cases = num_choose * rest_choose % MOD
    result = (result + sign * cases) % MOD


print(result)
