def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    
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
    
    answer = None
    while start <= end:
        mid = (start + end) // 2
        if solve(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer