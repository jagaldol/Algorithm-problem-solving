def solution(my_string):
    n = len(my_string)
    return "".join([my_string[n - i] for i in range(1, n + 1)])