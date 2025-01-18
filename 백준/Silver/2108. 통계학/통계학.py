import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]


def sol():
    numbers.sort()
    print(round(sum(numbers) / len(numbers)))
    print(numbers[len(numbers) // 2])
    counter = Counter(numbers)
    mode = counter.most_common()
    if len(numbers) > 1 and mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
    print(numbers[-1] - numbers[0])


sol()
