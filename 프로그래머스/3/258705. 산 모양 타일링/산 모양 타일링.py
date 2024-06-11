def solution(n, tops):
    answer = [0] * 100001
    real = [0] * 100001

    if n == 1:
        if tops[0] == 1:
            return 4
        else:
            return 3

    if tops[0] == 1:
        answer[0] = 3
        real[0] = 4
    else:
        answer[0] = 2
        real[0] = 3

    if n == 2:
        if tops[1] == 1:
            return answer[0] * 4 + 3
        else:
            return answer[0] * 3 + 2

    if tops[1] == 1:
        answer[1] = answer[0] * 3 + 2
        real[1] = answer[0] * 4 + 3
    else:
        answer[1] = answer[0] * 2 + 1
        real[1] = answer[0] * 3 + 2

    for i in range(2, n):
        if tops[i] == 1:
            case = 3
        else:
            case = 2
        answer[i] = (answer[i - 1] * case + real[i - 2] * (case - 1)) % 10007
        real[i] = (answer[i - 1] * (case + 1) + real[i - 2] * case) % 10007

    return real[n - 1]
