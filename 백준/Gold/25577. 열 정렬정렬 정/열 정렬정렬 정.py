import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = sorted(arr) #정렬된 arr

k = 0
count = 0
for i in range(n):
    if arr[i] == s[i]:
        k += 1
        continue
    temp = arr[i]
    obj = s[k]
    
    index = arr.index(obj)
    # swap
    arr[i] = obj
    arr[index] = temp
    k += 1
    count += 1

print(count)