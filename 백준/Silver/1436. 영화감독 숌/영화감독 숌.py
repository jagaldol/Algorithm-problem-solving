import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())


def sol():
    title_set = set()
    digit = 1
    while len(title_set) < N:
        for num in range(0, 10**digit):
            num_str = list(str(num).zfill(digit))
            for i in range(digit + 1):
                title_set.add(int("".join(num_str[:i] + ["666"] + num_str[i:])))

        digit += 1

    sorted_titles = sorted(list(title_set))
    print(sorted_titles[N - 1])


sol()
