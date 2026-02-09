def solution(num_list):
    n = len(num_list)
    return [num_list[n - i] for i in range(1, n + 1)]