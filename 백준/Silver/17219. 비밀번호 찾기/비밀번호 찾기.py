import sys

input = sys.stdin.readline

N, M = map(int, input().split())
passwords = [input().split() for _ in range(N)]


def sol():
    password_dict = {site: password.strip() for site, password in passwords}
    for _ in range(M):
        site = input().strip()
        print(password_dict[site])


sol()
