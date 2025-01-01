import sys

input = sys.stdin.readline

fizzbuzzs = [input().strip() for _ in range(3)]


def print_fizzbuzz(n):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


def sol():
    temps = [0, 0, 0]
    for i in range(3):
        if fizzbuzzs[i] == "FizzBuzz":
            # 15의 배수
            temps[i] = 15
        elif fizzbuzzs[i] == "Fizz":
            # 3의 배수
            temps[i] = 3
        elif fizzbuzzs[i] == "Buzz":
            # 5의 배수
            temps[i] = 5
        else:
            print_fizzbuzz(int(fizzbuzzs[i]) + 3 - i)
            return

    answer = 4
    while not (
        (answer - 3) % temps[0] == 0
        and (answer - 2) % temps[1]
        and (answer - 1) % temps[2] == 0
    ):
        answer += 1

    print_fizzbuzz(answer)


sol()
