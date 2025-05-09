import sys

input = sys.stdin.readline


def largest_rectangle(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, heights[top] * width)

    return max_area


while (line := input().strip()) != "0":
    arr = list(map(int, line.strip().split()))
    print(largest_rectangle(arr[1:]))
