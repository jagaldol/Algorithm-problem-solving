def solution(edges):
    link = [[] for _ in range(1000001)]
    reverse_link = [[] for _ in range(1000001)]

    candidates = set()

    for a, b in edges:
        link[a].append(b)
        reverse_link[b].append(a)
        if len(reverse_link[a]) == 0:
            candidates.add(a)

    created = 0
    for candidate in candidates:
        if len(reverse_link[candidate]) == 0 and len(link[candidate]) >= 2:
            created = candidate

    donut = stick = wave = 0

    for start in link[created]:
        now = start
        res = 0
        if len(link[now]) == 0:
            res = 2
        elif len(link[now]) > 1:
            res = 3
        while res == 0:
            now = link[now][0]
            if len(link[now]) == 0:
                res = 2
            elif len(link[now]) > 1:
                res = 3
            elif now == start:
                res = 1

        if res == 1:
            donut += 1
        elif res == 2:
            stick += 1
        else:
            wave += 1
    answer = [created, donut, stick, wave]
    return answer
