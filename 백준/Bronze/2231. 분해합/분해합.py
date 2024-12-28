N = input()


def sol():
    for i in range(1, int(N)):
        target = i + sum(map(int, list(str(i))))
        if target == int(N):
            print(i)
            return
    print(0)


sol()
