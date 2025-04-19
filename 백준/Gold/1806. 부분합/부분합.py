import sys

input = sys.stdin.readline
N, S = map(int, input().split())
A = list(map(int, input().split()))


def sol():
    start = 0
    end = 0
    answer = N + 1
    total = 0
    while end <= N:
        if total >= S:
            answer = min(answer, end - start)
            total -= A[start]
            start += 1
        else:
            end += 1
            if end <= N:
                total += A[end - 1]

    print(answer if answer != N + 1 else 0)


sol()
