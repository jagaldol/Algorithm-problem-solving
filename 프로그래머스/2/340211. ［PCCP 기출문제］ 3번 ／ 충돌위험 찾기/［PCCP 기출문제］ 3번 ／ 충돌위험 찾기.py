from collections import deque, Counter


def solution(points, routes):
    robots = [deque([tuple(points[point - 1]) for point in route]) for route in routes]
    
    answer = 0
    while robots:
        counter = Counter(robot[0] for robot in robots)
        answer += sum(value > 1 for key, value in counter.items())
        robots = [robot for robot in robots if len(robot) > 1]
        for robot in robots:
            nx, ny = robot[0]
            gx, gy = robot[1]
            if nx < gx:
                nx += 1
            elif nx > gx:
                nx -= 1
            elif ny < gy:
                ny += 1
            else:
                ny -= 1
            
            if (nx, ny) == (gx, gy):
                robot.popleft()
            else:
                robot[0] = (nx, ny)
    
    return answer