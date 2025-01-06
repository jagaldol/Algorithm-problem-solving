N = int(input())

# 1, 2, 3, 4


def sol():
    result = N // 5
    rest = N % 5
    if rest == 1:
        if result == 0:
            result = -1
        else:
            result += 1
        result - 1
    if rest == 2:
        if result < 2:
            result = -1
        else:
            result += 2
    if rest == 3:
        result += 1
    if rest == 4:
        if result == 0:
            result = -1
        else:
            result += 2

    print(result)


sol()
