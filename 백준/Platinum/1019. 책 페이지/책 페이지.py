N = int(input())


num = [0] * 10


def add_one_page(page, point):
    while page > 0:
        num[page % 10] += point
        page //= 10


def count_digits(n):
    point = 1
    while n > 0:
        while n > 0 and n % 10 != 9:
            add_one_page(n, point=point)
            n -= 1
        if n == 0:
            break
        for i in range(1, 10):
            num[i] += point

        n //= 10
        for i in range(10):
            num[i] += n * point
        point *= 10


count_digits(N)
print(*num)
