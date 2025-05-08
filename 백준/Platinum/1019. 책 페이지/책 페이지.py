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

        start = 1
        while start <= n and start % 10 != 0:
            add_one_page(start, point)
            start += 1
        if n < start:
            break
        cnt = n // 10 - start // 10 + 1
        for i in range(10):
            num[i] += cnt * point
        n //= 10
        point *= 10


count_digits(N)
print(*num)
