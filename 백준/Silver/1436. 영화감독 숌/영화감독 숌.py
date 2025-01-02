import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())


def sol():
    title_set = set()
    digit = 1
    while len(title_set) < N:
        for num in range(0, 10**digit):
            for title in permutations(["666"] + list(str(num).zfill(digit))):
                title_set.add(int("".join(title)))

        digit += 1

    sorted_titles = sorted(list(title_set))
    print(sorted_titles[N - 1])


sol()
