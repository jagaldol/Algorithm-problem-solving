import sys


def sol():
    input = sys.stdin.readline

    N = int(input())

    H = list(map(int, input().split()))

    arrows = {}

    result = 0

    for h in H:
        if h in arrows and arrows[h] > 0:
            arrows[h] -= 1
        else:
            result += 1

        if h - 1 in arrows and arrows[h - 1] > 0:
            arrows[h - 1] += 1
        else:
            arrows[h - 1] = 1

    print(result)


sol()
