from __future__ import annotations
import sys

input = sys.stdin.readline

RUDOLF = -1

N, M, P, C, D = map(int, input().split())
R = list(map(int, input().split()))
S_lst = [list(map(int, input().split())) for _ in range(P)]


class Board:
    def set_pieces(self, rudolf, santa_list):
        self.spaces = [[None] * (N + 1) for _ in range(N + 1)]
        self.spaces[rudolf.r][rudolf.c] = rudolf
        for santa in santa_list:
            self.spaces[santa.r][santa.c] = santa

        self.rudolf = rudolf
        self.santa_list = santa_list


board = Board()


def calculate_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


class Santa:
    def __init__(self, position, id):
        self.id = id
        self.r = position[0]
        self.c = position[1]
        self.stun = 0
        self.fall = False
        self.score = 0

    def move(self):
        if self.fall or self.stun != 0:
            return

        x, y = self.__get_move_direction()
        if x == y == 0:
            return

        nr, nc = self.r + x, self.c + y

        if board.spaces[nr][nc] != None:
            board.spaces[nr][nc] = self
            board.spaces[self.r][self.c] = None
            self.r, self.c = nr, nc
            self.collusion(-x, -y, D, D)
            board.spaces[nr][nc] = board.rudolf
        else:
            board.spaces[self.r][self.c], board.spaces[nr][nc] = None, self
            self.r, self.c = self.r + x, self.c + y

    def __get_move_direction(self):
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        rudolf = board.rudolf
        min_value = calculate_distance(self.r, self.c, rudolf.r, rudolf.c)

        x, y = 0, 0
        for tx, ty in directions:
            nr, nc = self.r + tx, self.c + ty
            if (
                1 <= nr <= N
                and 1 <= nc <= N
                and not isinstance(board.spaces[nr][nc], Santa)
            ):
                dist = calculate_distance(nr, nc, rudolf.r, rudolf.c)
                if dist < min_value:
                    min_value = dist
                    x, y = tx, ty

        return x, y

    def collusion(self, x, y, power, score):
        nr, nc = self.r + x * power, self.c + y * power
        self.score += score

        if score != 0:
            self.stun = 2

        if not (1 <= nr <= N and 1 <= nc <= N):
            self.fall = True
            board.spaces[self.r][self.c] = None
            return

        if board.spaces[nr][nc] != None:
            board.spaces[nr][nc].collusion(x, y, 1, 0)

        board.spaces[self.r][self.c], board.spaces[nr][nc] = None, self
        self.r, self.c = nr, nc

    def raise_score(self):
        if not self.fall:
            self.score += 1


class Rudolf:
    def __init__(self, position):
        self.r = position[0]
        self.c = position[1]

    def move(self):
        santa: Santa = self.__select_nearest()
        x, y = self.__get_move_direction(santa)
        nr, nc = self.r + x, self.c + y

        if board.spaces[nr][nc] != None:
            santa.collusion(x, y, C, C)

        board.spaces[self.r][self.c], board.spaces[nr][nc] = None, self
        self.r, self.c = self.r + x, self.c + y

    def __select_nearest(self):
        return min(
            (
                calculate_distance(self.r, self.c, santa.r, santa.c),
                -santa.r,
                -santa.c,
                santa,
            )
            for santa in board.santa_list
            if not santa.fall
        )[3]

    def __get_move_direction(self, santa: Santa):
        if santa.r > self.r:
            x = 1
        elif santa.r < self.r:
            x = -1
        else:
            x = 0
        if santa.c > self.c:
            y = 1
        elif santa.c < self.c:
            y = -1
        else:
            y = 0

        return x, y


def solution():
    rudolf = Rudolf(R)
    santa_list: list[Santa] = []

    for id, r, c in S_lst:
        santa_list.append(Santa((r, c), id))

    santa_list.sort(key=lambda x: x.id)

    board.set_pieces(rudolf, santa_list)

    for _ in range(M):

        if sum(1 for santa in santa_list if not santa.fall) == 0:
            break
        rudolf.move()
        if sum(1 for santa in santa_list if not santa.fall) == 0:
            break
        for santa in santa_list:
            santa.move()
        for santa in santa_list:
            if santa.stun > 0:
                santa.stun -= 1
            santa.raise_score()

    for santa in santa_list:
        print(santa.score, end=" ")
    print()


solution()
