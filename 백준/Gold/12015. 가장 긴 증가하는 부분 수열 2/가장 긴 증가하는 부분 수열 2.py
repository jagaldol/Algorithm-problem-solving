import bisect

N = int(input())
A = list(map(int, input().split()))


def sol():
    dp = [A[0]]

    for i in range(1, N):
        if A[i] > dp[-1]:
            dp.append(A[i])
        else:
            idx = bisect.bisect_left(dp, A[i])
            dp[idx] = A[i]
    print(len(dp))


sol()
