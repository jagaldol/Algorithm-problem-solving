def solution(name, yearning, photo):
    scores = {n: score for n, score in zip(name, yearning)}
    return [sum(scores[n] if n in scores.keys() else 0 for n in p) for p in photo]
    