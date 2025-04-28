x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def ccw(p1, p2, p3):
    v = (p2[0] - p1[0], p2[1] - p1[1])
    u = (p3[0] - p1[0], p3[1] - p1[1])
    return v[0] * u[1] - v[1] * u[0]


con1 = ccw((x1, y1), (x2, y2), (x3, y3)) * ccw((x1, y1), (x2, y2), (x4, y4))
con2 = ccw((x3, y3), (x4, y4), (x1, y1)) * ccw((x3, y3), (x4, y4), (x2, y2))
if con1 > 0 or con2 > 0:
    print(0)
elif con1 == 0 and con2 == 0:
    min_x1, max_x1 = min(x1, x2), max(x1, x2)
    min_y1, max_y1 = min(y1, y2), max(y1, y2)
    min_x2, max_x2 = min(x3, x4), max(x3, x4)
    min_y2, max_y2 = min(y3, y4), max(y3, y4)

    if min_x1 <= max_x2 and min_x2 <= max_x1 and min_y1 <= max_y2 and min_y2 <= max_y1:
        print(1)
    else:
        print(0)
else:
    print(1)
