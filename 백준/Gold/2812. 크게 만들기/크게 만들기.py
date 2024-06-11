def sol():
    N, K = map(int, input().split())
    num = input().rstrip()

    stack = []

    for idx, number in enumerate(num):
        if K == 0:
            print("".join(stack) + num[idx:])
            return
        while stack and K and stack[-1] < number:
            stack.pop()
            K -= 1
        stack.append(number)
    if K:
        print("".join(stack[:-K]))
    else:
        print("".join(stack))


sol()
