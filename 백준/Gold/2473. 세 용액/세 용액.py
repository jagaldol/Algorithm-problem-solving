n = int(input())
arr = list(map(int, input().split()))
arr.sort()

minAbsTotal = int(3e9)
res = None

for i in range(1, n-1):
    base = arr[i-1]
    left = i
    right = n-1
    while left < right:
        total = base + arr[left] + arr[right]
        absTotal = abs(total)
        if absTotal < minAbsTotal:
            minAbsTotal = absTotal
            res = (base, arr[left], arr[right])

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else: break
    else: continue
    break
print(" ".join(map(str, res)))