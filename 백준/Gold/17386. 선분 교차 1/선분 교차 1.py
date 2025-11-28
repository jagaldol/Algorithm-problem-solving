l1 = tuple(map(int, input().split()))
l2 = tuple(map(int, input().split()))


def ccw(p1, p2, p3):
    x1, x2 = p2[0] - p1[0], p2[1] - p1[1]
    y1, y2 = p3[0] - p1[0], p3[1] - p1[1]
    return x1 * y2 - x2 * y1


def sol():
    l1p1 = l1[:2]
    l1p2 = l1[2:]
    l2p1 = l2[:2]
    l2p2 = l2[2:]

    if ccw(l1p1, l1p2, l2p1) * ccw(l1p1, l1p2, l2p2) < 0 and ccw(l2p1, l2p2, l1p1) * ccw(l2p1, l2p2, l1p2) < 0:
        print(1)
    else:
        print(0)


sol()
