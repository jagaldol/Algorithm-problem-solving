def solution(n):
    d = n % 2
    if d:
        n -= 1
    return (n // 2 + 1) * n // 2