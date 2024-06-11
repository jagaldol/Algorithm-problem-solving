def isInPlanet(cx, cy, r, x, y):
    distance = (cx - x)**2 + (cy - y)**2
    if (distance > r**2):
        return False
    else:
        return True

def solution():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    result = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        isIn1 = isInPlanet(cx, cy, r, x1, y1)
        isIn2 = isInPlanet(cx, cy, r, x2, y2)
        # XOR
        if (isIn1 ^ isIn2):
            result += 1
    
    print(result)

def main():
    T = int(input())
    for _ in range(T):
        solution()

main()