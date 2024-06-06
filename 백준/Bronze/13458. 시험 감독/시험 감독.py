import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def sol():
    answer = N
    for a in A:
        if (remain := a - B) > 0:
            answer += math.ceil(remain / C)
    print(answer)


sol()
