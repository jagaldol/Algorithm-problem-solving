def input_process():
    N, M, B = map(int, input().split())

    heights = []

    for i in range(N):
        row = list(map(int, input().split()))
        heights.append(row)

    return N, M, B, heights


def calculate_time(N, M, B, heights, target):
    time = 0

    for i in range(N):
        for j in range(M):
            gap = target - heights[i][j]
            B -= gap
            time += gap if gap > 0 else -2 * gap
    
    return time, B


if __name__ == "__main__":
    N, M, B, heights = input_process()

    min_height, max_height = min(map(min, heights)), max(map(max, heights))

    min_time = 200000000
    max_target = 0
    for target in range(min_height, max_height + 1):
        time, remain_block = calculate_time(N, M, B, heights, target)
        if remain_block < 0:
            continue
        if time < min_time:
            min_time = time
            max_target = target
        elif time == min_time and max_target < target:
            max_target = target

    print(min_time, max_target)