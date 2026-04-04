def solution(array, height):
    return sum(1 for h in array if h > height)