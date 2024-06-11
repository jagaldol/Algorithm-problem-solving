import math

def calculate(fees, time):
    if time > fees[0]:
        return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
    return fees[1]

def solution(fees, records):
    times = {}
    
    for record in records:
        time_str, number, io = record.split()
        HH, MM = map(int, time_str.split(":"))
        time = (23 - HH) * 60 + (59 - MM)
        if io == "IN":
            if number in times:
                times[number] += time
            else:
                times[number] = time
        else:
            times[number] -= time
    
    return [calculate(fees, val) for key, val in sorted(times.items())]