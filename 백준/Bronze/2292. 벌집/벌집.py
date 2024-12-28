N = int(input())


def sol():
    step = 1
    while 3 * step**2 - 3 * step + 1 < N:
        step += 1
    print(step)


sol()
