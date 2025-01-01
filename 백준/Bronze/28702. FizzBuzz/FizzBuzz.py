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
    for i, fizzbuzz in enumerate(fizzbuzzs):
        if fizzbuzz not in ("FizzBuzz", "Fizz", "Buzz"):
            print_fizzbuzz(int(fizzbuzz) + 3 - i)
            return


sol()
