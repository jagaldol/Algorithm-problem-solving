import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


def sol():
    li = [(0, 0)]

    for a in A:
        li.append((a, max([count for h, count in li if h < a]) + 1))

    print(max(count for h, count in li))


sol()
