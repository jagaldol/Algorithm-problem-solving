N, M = map(int, input().split())
board = [input() for _ in range(N)]

answer = 11

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class State:
    def __init__(self, rx, ry, bx, by):
        self.rx = rx
        self.ry = ry
        self.bx = bx
        self.by = by

    def __eq__(self, other):
        return (
            self.rx == other.rx
            and self.ry == other.ry
            and self.bx == other.bx
            and self.by == other.by
        )

    def copy(self):
        return State(self.rx, self.ry, self.bx, self.by)


def dfs(path: list[State]):
    global answer
    if len(path) >= answer:
        return
    now = path[-1]
    for tx, ty in steps:
        next = now.copy()
        red_hole, blue_hole = False, False
        while True:
            nbx, nby = next.bx + tx, next.by + ty
            nrx, nry = next.rx + tx, next.ry + ty
            if board[nbx][nby] != "#" and board[nrx][nry] != "#":
                next.bx = nbx
                next.by = nby
                next.rx = nrx
                next.ry = nry
            elif (
                board[nbx][nby] == "#"
                and board[nrx][nry] != "#"
                and (not (nrx == next.bx and nry == next.by) or blue_hole)
            ):
                next.rx = nrx
                next.ry = nry
            elif (
                board[nrx][nry] == "#"
                and board[nbx][nby] != "#"
                and (not (nbx == next.rx and nby == next.ry) or red_hole)
            ):
                next.bx = nbx
                next.by = nby
            else:
                break

            if board[next.rx][next.ry] == "O":
                red_hole = True

            if board[next.bx][next.by] == "O":
                blue_hole = True
        if blue_hole:
            continue
        if red_hole:
            answer = len(path)
            return
        if next in path:
            continue
        path.append(next)
        dfs(path)
        path.pop()


def sol():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "B":
                bx, by = i, j
    dfs([State(rx, ry, bx, by)])

    print(answer if answer != 11 else -1)


sol()
