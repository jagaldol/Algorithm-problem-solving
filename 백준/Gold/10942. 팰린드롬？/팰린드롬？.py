import sys


def dp(num_list, N):
    is_palindrome = [[False if i != j else True for i in range(N)] for j in range(N)]

    for i in range(N):
        left = i - 1
        right = i + 1
        while left >= 0 and right <= N - 1:
            is_palindrome[left][right] = (
                is_palindrome[left + 1][right - 1] and num_list[left] == num_list[right]
            )

            left -= 1
            right += 1

    for i in range(N - 1):
        if num_list[i] == num_list[i + 1]:
            is_palindrome[i][i + 1] = True
    for i in range(N - 3):
        left = i
        right = i + 3
        while left >= 0 and right <= N - 1:
            is_palindrome[left][right] = (
                is_palindrome[left + 1][right - 1] and num_list[left] == num_list[right]
            )

            left -= 1
            right += 1
    return is_palindrome


def sol():
    input = sys.stdin.readline
    N = int(input())

    num_list = list(map(int, input().split()))

    is_palindrome = dp(num_list, N)

    M = int(input())

    for i in range(M):
        S, E = map(int, input().split())
        print(1 if is_palindrome[S - 1][E - 1] else 0)


sol()
