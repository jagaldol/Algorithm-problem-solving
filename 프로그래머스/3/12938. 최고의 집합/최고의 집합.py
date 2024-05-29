def solution(n, s):
    if n > s:
        return [-1]
    return [s//n if (n-i) > s%n else s//n+1 for i in range(n)]