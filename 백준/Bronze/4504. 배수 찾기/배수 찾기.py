def main():
    a = int(input())
    while True:
        b = int(input())
        if b == 0:
            break
        else:
            com(b, a)


def com(b, a):
    if b % a == 0:
        print(f"{b} is a multiple of {a}.")
    else :
        print(f"{b} is NOT a multiple of {a}.")


main()
