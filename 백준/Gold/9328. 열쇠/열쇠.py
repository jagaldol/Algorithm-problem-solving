from collections import deque

T = int(input())

steps = [(1, 0), (0, -1), (-1, 0), (0, 1)]

answer = 0

retry = False


def open_door(building, key: str):
    global retry
    retry = True
    door = key.upper()
    for row in building:
        for i in range(len(row)):
            if row[i] == door:
                row[i] = "."


def dfs(building, visited, x, y):
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if not visited[nx][ny]:
            if building[nx][ny] == "$":
                global answer
                answer += 1
                building[nx][ny] = "."
            if building[nx][ny].islower():
                key = building[nx][ny]
                open_door(building, key)
                building[nx][ny] = "."
            if building[nx][ny] == ".":
                visited[nx][ny] = True
                dfs(building, visited, nx, ny)


def print_building(building):
    for row in building:
        print("".join(row))
    print()


for _ in range(T):
    retry = True
    answer = 0
    h, w = map(int, input().split())
    building = [["*" for _ in range(w + 2)] for _ in range(h + 2)]
    for i in range(1, h + 1):
        row = input()
        for j in range(1, w + 1):
            building[i][j] = row[j - 1]
    keys = input()

    if not keys == "0":
        for key in keys:
            open_door(building, key)

    queue = deque()
    for i in range(1, h + 1):
        if building[i][1] != "*":
            queue.append((i, 1))
        if building[i][w] != "*":
            queue.append((i, w))

    for j in range(2, w):
        if building[1][j] != "*":
            queue.append((1, j))
        if building[h][j] != "*":
            queue.append((h, j))

    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]

    for x, y in queue:
        if building[x][y] == "$":
            answer += 1
            building[x][y] = "."
        if building[x][y].islower():
            key = building[x][y]
            open_door(building, key)
            building[x][y] = "."
        if building[x][y] == ".":
            visited[x][y] = True

    while retry:
        retry = False
        temp = deque()

        while queue:
            x, y = queue.popleft()
            if building[x][y].isupper():
                temp.append((x, y))
                continue
            if any(building[x + dx][y + dy].isupper() for dx, dy in steps):
                temp.append((x, y))

            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                if not visited[nx][ny]:
                    if building[nx][ny] == "$":
                        answer += 1
                        building[nx][ny] = "."
                    if building[nx][ny].islower():
                        key = building[nx][ny]
                        open_door(building, key)
                        building[nx][ny] = "."
                    if building[nx][ny] == ".":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        queue = temp

    print(answer)
