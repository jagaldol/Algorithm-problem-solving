def solution(friends, gifts):
    score = {}
    index = {}
    gift_log = [[0] * 50 for _ in range(50)]
    for i, friend in enumerate(friends):
        score[friend] = 0
        index[friend] = i

    for gift in gifts:
        A, B = gift.split()
        score[A] += 1
        score[B] -= 1
        gift_log[index[A]][index[B]] += 1

    expect = [0] * 50
    for A_i in range(len(friends)):
        for B_i in range(A_i + 1, len(friends)):
            if gift_log[A_i][B_i] > gift_log[B_i][A_i]:
                expect[A_i] += 1
            elif gift_log[A_i][B_i] < gift_log[B_i][A_i]:
                expect[B_i] += 1
            else:
                if score[friends[A_i]] > score[friends[B_i]]:
                    expect[A_i] += 1
                elif score[friends[A_i]] < score[friends[B_i]]:
                    expect[B_i] += 1

    return max(expect)
