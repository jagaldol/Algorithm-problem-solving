import sys

input = sys.stdin.readline

l = int(input())
n = int(input())
t = float(input())

speeds = [map(float, input().split()) for _ in range(n)]


def sol():
    for f, b in speeds:
        forward_time = l / f
        backward_time = l / b
        total_time = forward_time + backward_time

        if total_time < t:
            print("HOPE")
            return
    print("DOOMED")


sol()
