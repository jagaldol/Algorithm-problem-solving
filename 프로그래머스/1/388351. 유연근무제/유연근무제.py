def solution(schedules, timelogs, startday):
    def add_minutes(time, minutes):
        hour = time // 100
        minute = time % 100
        minute += minutes
        hour += minute // 60
        minute %= 60
        return hour * 100 + minute

    answer = 0
    for schedule, timelog in zip(schedules, timelogs):
        deadline = add_minutes(schedule, 10)
        is_late = False
        for i in range(7):
            weekday = (startday + i - 1) % 7 + 1  # 1~7 범위 유지
            if weekday in [6, 7]:
                continue  # 주말 제외
            if timelog[i] > deadline:
                is_late = True
                break
        if not is_late:
            answer += 1
    return answer