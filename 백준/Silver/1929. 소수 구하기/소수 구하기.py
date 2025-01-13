M, N = map(int, input().split())


def sol():
    numbers = [True for _ in range(1_000_001)]
    primes = []
    for n in range(2, N + 1):
        if numbers[n]:
            primes.append(n)
            for i in range(2, int(N / n) + 1):
                numbers[n * i] = False
    for prime in primes:
        if prime < M:
            continue
        print(prime)


sol()
