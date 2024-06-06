import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = input().split()


class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.right = 0
        self.left = 0
        self.front = 0
        self.rear = 0

    def roll_front(self):
        self.front, self.bottom, self.rear, self.top = (
            self.top,
            self.front,
            self.bottom,
            self.rear,
        )

    def roll_rear(self):
        self.rear, self.top, self.front, self.bottom = (
            self.top,
            self.front,
            self.bottom,
            self.rear,
        )

    def roll_left(self):
        self.left, self.bottom, self.right, self.top = (
            self.top,
            self.left,
            self.bottom,
            self.right,
        )

    def roll_right(self):
        self.right, self.top, self.left, self.bottom = (
            self.top,
            self.left,
            self.bottom,
            self.right,
        )


def sol():
    global x, y

    dice = Dice()

    for cmd in commands:
        if cmd == "1" and y + 1 in range(m):
            nx, ny = x, y + 1
            dice.roll_right()
        elif cmd == "2" and y - 1 in range(m):
            nx, ny = x, y - 1
            dice.roll_left()
        elif cmd == "3" and x - 1 in range(n):
            nx, ny = x - 1, y
            dice.roll_rear()
        elif cmd == "4" and x + 1 in range(n):
            nx, ny = x + 1, y
            dice.roll_front()
        else:
            nx, ny = x, y

        if nx != x or ny != y:
            x, y = nx, ny
            if board[nx][ny] == 0:
                board[nx][ny] = dice.bottom
            else:
                dice.bottom, board[nx][ny] = board[nx][ny], 0
            print(dice.top)


sol()
