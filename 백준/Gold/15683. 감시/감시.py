import sys

result = 64


def dfs(office_map, camera_positions, depth):
    if depth == len(camera_positions):
        count = sum(1 for row in office_map for element in row if element == 0)
        global result
        result = min(result, count)
        return

    camera_x, camera_y = camera_positions[depth]
    camera_type = office_map[camera_x][camera_y]

    empty_space = [[], [], [], []]  # right, left, bottom, top

    dx = [1, -1, 0, 0]  # right, left, bottom, top
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx, ny = camera_x + dx[i], camera_y + dy[i]
        while 0 <= nx < len(office_map) and 0 <= ny < len(office_map[0]):
            if office_map[nx][ny] == 6:
                break
            if office_map[nx][ny] == 0:
                empty_space[i].append((nx, ny))

            nx, ny = nx + dx[i], ny + dy[i]

    if camera_type == 1:
        for i in range(4):
            for x, y in empty_space[i]:
                office_map[x][y] = -1
            dfs(office_map, camera_positions, depth + 1)
            for x, y in empty_space[i]:
                office_map[x][y] = 0
    elif camera_type == 2:
        for d1, d2 in [[0, 1], [2, 3]]:
            for x, y in [*empty_space[d1], *empty_space[d2]]:
                office_map[x][y] = -1
            dfs(office_map, camera_positions, depth + 1)
            for x, y in [*empty_space[d1], *empty_space[d2]]:
                office_map[x][y] = 0
    elif camera_type == 3:
        for d1, d2 in [[0, 2], [2, 1], [1, 3], [3, 0]]:
            for x, y in [*empty_space[d1], *empty_space[d2]]:
                office_map[x][y] = -1
            dfs(office_map, camera_positions, depth + 1)
            for x, y in [*empty_space[d1], *empty_space[d2]]:
                office_map[x][y] = 0
    elif camera_type == 4:
        for d1, d2, d3 in [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]:
            for x, y in [*empty_space[d1], *empty_space[d2], *empty_space[d3]]:
                office_map[x][y] = -1
            dfs(office_map, camera_positions, depth + 1)
            for x, y in [*empty_space[d1], *empty_space[d2], *empty_space[d3]]:
                office_map[x][y] = 0
    elif camera_type == 5:
        for x, y in [
            *empty_space[0],
            *empty_space[1],
            *empty_space[2],
            *empty_space[3],
        ]:
            office_map[x][y] = -1
        dfs(office_map, camera_positions, depth + 1)
        for x, y in [
            *empty_space[0],
            *empty_space[1],
            *empty_space[2],
            *empty_space[3],
        ]:
            office_map[x][y] = 0


def sol():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    office_map = []
    for _ in range(N):
        office_map.append(list(map(int, input().split())))

    camera_positions = []

    for i in range(N):
        for j in range(M):
            if office_map[i][j] != 0 and office_map[i][j] != 6:
                camera_positions.append((i, j))

    dfs(office_map, camera_positions, 0)

    print(result)


sol()
