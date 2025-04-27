import sys
from itertools import product

input = sys.stdin.readline
n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


def sol():
    AB = sorted(a + b for a, b in product(A, B))
    CD = sorted(c + d for c, d in product(C, D))

    answer = 0

    left = 0
    right = len(AB) - 1
    while left < len(AB) and right >= 0:
        total_sum = AB[left] + CD[right]
        if total_sum == 0:
            ab_count = 1
            cd_count = 1
            while left < len(AB) - 1 and AB[left] == AB[left + 1]:
                left += 1
                ab_count += 1
            while right > 0 and CD[right] == CD[right - 1]:
                right -= 1
                cd_count += 1
            answer += ab_count * cd_count
            if right > 0:
                right -= 1
            else:
                left += 1
        elif total_sum < 0:
            left += 1
        else:
            right -= 1

    print(answer)


sol()
