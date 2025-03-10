import sys

input = sys.stdin.readline

N = int(input())
items = list(map(int, input().split()))


def sol():
    signed_items = sorted([(item, 1) if item >= 0 else (-item, -1) for item in items])
    min_value = 2_000_000_000
    result = (0, 0)
    for i in range(N - 1):
        item1, sign1 = signed_items[i]
        item2, sign2 = signed_items[i + 1]
        if (value := abs(sign1 * item1 + sign2 * item2)) < min_value:
            min_value = value
            result = (sign1 * item1, sign2 * item2)

    if result[0] < result[1]:
        print(result[0], result[1])
    else:
        print(result[1], result[0])


sol()
