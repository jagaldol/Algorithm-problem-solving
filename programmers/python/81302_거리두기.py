arounds = [[-2, 0], [-1, -1], [0, -2], [1, -1], [2, 0], [1, 1], [0, 2], [-1, 1]]

arounds_allow = [
    [[-1, 0]],
    [[0, -1], [-1, 0]],
    [[0, -1]],
    [[0, -1], [1, 0]],
    [[1, 0]],
    [[0, 1], [1, 0]],
    [[0, 1]],
    [[0, 1], [-1, 0]],
]

nears = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def solution(places):
    answer = []
    for place in places:
        if isBad(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer


def isBad(place):
    for i in range(5):
        for j in range(5):
            now = place[i][j]
            if now == "P":
                if HasNear(place, i, j):
                    return True
    return False


def HasNear(place, i, j):
    for near in nears:
        x = i + near[0]
        y = j + near[1]
        if not (0 <= x < 5) or not (0 <= y < 5):
            continue
        if place[x][y] == "P":
            return True

    for idx in range(len(arounds)):
        x = i + arounds[idx][0]
        y = j + arounds[idx][1]
        if not (0 <= x < 5) or not (0 <= y < 5):
            continue
        if place[x][y] == "P":
            if not exist_partition(place, i, j, idx):
                return True
    return False


def exist_partition(place, i, j, idx):
    check_list = arounds_allow[idx]

    for offset in check_list:
        if place[i + offset[0]][j + offset[1]] != "X":
            return False
    return True
