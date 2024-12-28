N = input()


def sol():
    for i in range(max(1, int(N) - 9 * len(N)), int(N)):
        target = i + sum(map(int, str(i)))
        if target == int(N):
            print(i)
            return
    print(0)


sol()
