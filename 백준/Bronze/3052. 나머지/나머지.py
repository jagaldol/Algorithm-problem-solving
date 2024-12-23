nums = [int(input()) for _ in range(10)]
print(len(set(num % 42 for num in nums)))
