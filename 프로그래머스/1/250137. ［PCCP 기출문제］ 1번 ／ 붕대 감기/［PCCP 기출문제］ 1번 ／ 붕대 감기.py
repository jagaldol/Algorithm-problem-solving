def solution(bandage, health, attacks):
    max_health = health
    
    streak = 0
    next_attack = 0
    for t in range(attacks[-1][0]):
        if t + 1 == attacks[next_attack][0]:
            health -= attacks[next_attack][1]
            next_attack += 1
            if health <= 0:
                return -1
            
            streak = 0
            continue
        streak += 1
        health += bandage[1]
        if streak == bandage[0]:
            health += bandage[2]
            streak = 0
        health = min(health, max_health)
    return health