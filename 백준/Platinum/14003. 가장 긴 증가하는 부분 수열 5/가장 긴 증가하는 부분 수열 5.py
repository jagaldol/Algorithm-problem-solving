import bisect

N = int(input())
A = list(map(int, input().split()))


def sol():
    dp = [A[0]]
    lis = [0] * N
    lis[0] = 1

    for i in range(1, N):
        if A[i] > dp[-1]:
            dp.append(A[i])
            lis[i] = len(dp)
        else:
            idx = bisect.bisect_left(dp, A[i])
            dp[idx] = A[i]
            lis[i] = idx + 1
    target = len(dp)
    answer = []
    for i in range(N - 1, -1, -1):
        if lis[i] == target:
            answer.append(A[i])
            target -= 1
            if target == 0:
                break
    print(len(answer))
    print(*answer[::-1])


sol()
