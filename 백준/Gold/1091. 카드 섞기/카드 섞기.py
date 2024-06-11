import sys


class Card:
    def __init__(self, start, target_player):
        self.start = start
        self.location = start
        self.target_player = target_player


def shuffle(deck: list[Card], S: list):
    for card in deck:
        card.location = S[card.location]


def check_success(deck: list[Card]):
    for card in deck:
        if card.location % 3 != card.target_player:
            return False
    return True


def check_stop(deck: list[Card]):
    for card in deck:
        if card.location != card.start:
            return False
    return True


def sol():
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))

    deck = [Card(idx, target) for idx, target in enumerate(P)]

    count = 0
    while True:
        if check_success(deck):
            print(count)
            break
        shuffle(deck, S)
        count += 1
        if check_stop(deck):
            print(-1)
            break


sol()
