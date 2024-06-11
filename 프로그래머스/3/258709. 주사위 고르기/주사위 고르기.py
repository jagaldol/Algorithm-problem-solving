from itertools import combinations, product


def compare(a_possible, b_possible):
    count = 0
    for a in a_possible:
        left = 0
        right = len(b_possible)
        while left < right:
            center = (left + right) // 2
            if a > b_possible[center]:
                left = center + 1
            else:
                right = center
        count += left

    return count


def solution(dice):
    possible = {}

    for comb in combinations(range(len(dice)), len(dice) // 2):
        half_dice = [dice[i] for i in comb]

        possible[" ".join(map(str, comb))] = sorted(
            [sum(combination) for combination in product(*half_dice)]
        )

    best = []
    best_win_score = 0

    for comb in combinations(range(len(dice)), len(dice) // 2):
        A_dice_index = list(comb)
        B_dice_index = [i for i in range(len(dice)) if i not in A_dice_index]

        result = compare(
            possible[" ".join(map(str, A_dice_index))],
            possible[" ".join(map(str, B_dice_index))],
        )
        if result > best_win_score:
            best_win_score = result
            best = A_dice_index

    answer = [i + 1 for i in best]
    return answer
