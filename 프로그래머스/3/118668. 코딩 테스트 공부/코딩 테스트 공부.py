def solution(alp, cop, problems):
    target_alp = max(p[0] for p in problems)
    target_cop = max(p[1] for p in problems)

    # 이미 목표를 넘은 능력치는 목표와 같게 취급
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    # dp[a][c]: 능력치 (a, c)에 도달하는 최소 시간
    dp = [
        [float("inf")] * (target_cop + 1)
        for _ in range(target_alp + 1)
    ]
    dp[alp][cop] = 0

    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):
            # 1. 알고력 공부: 시간 1, 알고력 +1
            if a < target_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)

            # 2. 코딩력 공부: 시간 1, 코딩력 +1
            if c < target_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 3. 현재 능력으로 풀 수 있는 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a < alp_req or c < cop_req:
                    continue

                na = min(target_alp, a + alp_rwd)
                nc = min(target_cop, c + cop_rwd)

                dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)

    return dp[target_alp][target_cop]