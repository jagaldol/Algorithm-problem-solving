import math


def sol():
    A, B = map(int, input().split())

    limit = int(math.sqrt(B))

    i_limit = (limit + 1) // 2
    checks = [0] * i_limit
    primes = [2]

    for i in range(1, i_limit):
        if checks[i]:
            continue
        p = 2 * i + 1
        primes.append(p)

        idx = i
        while idx < i_limit:
            checks[idx] = 1
            idx += p

    count = 0
    for prime in primes:
        value = prime * prime
        while value <= B:
            if A <= value:
                count += 1
            value *= prime

    print(count)


sol()
