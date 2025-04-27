import sys

input = sys.stdin.readline
n = int(input())
A, B, C, D = [0] * n, [0] * n, [0] * n, [0] * n
for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, input().split())


def sol():
    AB = sorted(a + b for a in A for b in B)
    CD = sorted(c + d for c in C for d in D)
    length = len(AB)

    answer = 0

    left = 0
    right = length - 1
    while left < length and right >= 0:
        total_sum = AB[left] + CD[right]
        if total_sum == 0:
            ab_count = 1
            cd_count = 1
            while left < length - 1 and AB[left] == AB[left + 1]:
                left += 1
                ab_count += 1
            while right > 0 and CD[right] == CD[right - 1]:
                right -= 1
                cd_count += 1
            answer += ab_count * cd_count
            left += 1
            right -= 1
        elif total_sum < 0:
            left += 1
        else:
            right -= 1

    print(answer)


sol()
