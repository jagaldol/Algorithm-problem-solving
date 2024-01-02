import sys, heapq


def sol():
    input = sys.stdin.readline

    N = int(input())

    card_lists = []
    for i in range(N):
        heapq.heappush(card_lists, int(input()))

    result = 0

    for i in range(N - 1):
        first = heapq.heappop(card_lists)
        second = heapq.heappop(card_lists)

        sum = first + second
        result += sum
        heapq.heappush(card_lists, sum)

    print(result)


sol()
