import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]


def binary_search(start, end):
    mid = (start + end) // 2
    if start == mid:
        if mid < end and sum(lan // end for lan in lans) >= N:
            print(end)
        else:
            print(mid)
        return
    count = sum(lan // mid for lan in lans)
    if count < N:
        binary_search(start, mid - 1)
    else:
        binary_search(mid, end)


def sol():
    binary_search(1, sum(lans) // N)


sol()
