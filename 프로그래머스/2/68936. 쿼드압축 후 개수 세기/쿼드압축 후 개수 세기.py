def divide(arr):
    half = len(arr) // 2
    up_left = [row[:half] for row in arr[:half]]
    up_right = [row[half:] for row in arr[:half]]
    down_left = [row[:half] for row in arr[half:]]
    down_right = [row[half:] for row in arr[half:]]
    
    if half == 0:
        return (0, 1) if arr[0][0] == 1 else (1, 0)
    
    zeros, ones = [sum(elem) for elem in zip(divide(up_left), divide(up_right), divide(down_left), divide(down_right))]
    if zeros == 4 and ones == 0:
        return 1, 0
    if zeros == 0 and ones == 4:
        return 0, 1
    return zeros, ones


def solution(arr):
    return divide(arr)