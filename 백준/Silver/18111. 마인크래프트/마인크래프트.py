def input_process():
    N, M, B = map(int, input().split())

    counts = [0] * 257

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            counts[row[j]] += 1

    return N, M, B, counts


def sol():
    N, M, B, counts = input_process()

    min_time = 200000000
    max_target = 0

    for target in range(257):
        low = high = 0
        for i in range(0, 257):
            cost = abs(target - i) * counts[i]
            if (i < target):
                low += cost
            else:
                high += cost

        if high + B >= low:
            time = high * 2 + low
            if time <= min_time:
                min_time, max_target = time, target

    print(min_time, max_target)

sol()