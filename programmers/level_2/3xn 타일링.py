def solution(n):
    prev = (1, 2)

    for i in range(1, n // 2):
        prev = (
            (prev[0] + prev[1]) % 1_000_000_007,
            (prev[0] * 2 + prev[1] * 3) % 1_000_000_007,
        )

    answer = (prev[0] + prev[1]) % 1_000_000_007

    return answer
