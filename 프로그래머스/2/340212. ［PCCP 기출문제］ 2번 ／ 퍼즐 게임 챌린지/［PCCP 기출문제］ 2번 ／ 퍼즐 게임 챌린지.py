def solution(diffs, times, limit):
    start = 1
    end = limit
    
    def solve(level):
        time_prev = 0
        time = 0
        for diff, time_cur in zip(diffs, times):
            if diff > level:
                time += (diff - level) * (time_cur + time_prev)
            time += time_cur
            if time > limit:
                return False
            time_prev = time_cur
        return True
    
    while start < end:
        mid = (start + end) // 2
        if solve(mid):
            end = mid
        else:
            start = mid + 1
    
    return end