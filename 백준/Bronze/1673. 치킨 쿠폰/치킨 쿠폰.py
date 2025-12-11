import sys


def calculate(n, k):
    ans = n
    while n // k > 0:
        ans += n // k
        remain = n % k
        n = (n // k) + remain
    return ans


while inp := sys.stdin.readline():
    n, k = map(int, inp.split())
    print(calculate(n, k))
