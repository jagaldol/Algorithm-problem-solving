from collections import Counter

T = int(input())

for i in range(T):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt - 1)
