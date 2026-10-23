def solution(s):
    opend = 0
    for c in s:
        if c == "(":
            opend += 1
        else:
            opend -= 1
        if opend < 0:
            return False
    if opend != 0:
        return False
    return True