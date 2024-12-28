L = int(input())
string = input()
r = 31
M = 1234567891


def sol():
    H = 0
    for i, s in enumerate(string):
        a = ord(s) - ord("a") + 1
        H += (a * r**i) % M
    print(H % M)


sol()
