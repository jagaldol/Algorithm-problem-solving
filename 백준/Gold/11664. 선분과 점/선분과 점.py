import sys, math


def length(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)


def b_search(start, end, C):
    left_length = round(length(start, C), 11)
    right_length = round(length(C, end), 11)

    middle = [(start[i] + end[i]) / 2 for i in range(3)]

    if left_length < right_length:
        b_search(start, middle, C)
    elif left_length > right_length:
        b_search(middle, end, C)
    else:
        print(f"{length(middle, C):.10f}")


def sol():
    input = sys.stdin.readline

    Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

    b_search([Ax, Ay, Az], [Bx, By, Bz], [Cx, Cy, Cz])


sol()
