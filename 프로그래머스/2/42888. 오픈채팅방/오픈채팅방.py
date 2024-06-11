def solution(record):
    uid_name_map = {}
    for log in record:
        splited_log = log.split()
        if len(splited_log) <= 2: continue
        
        uid_name_map[splited_log[1]] = splited_log[2]
    
    answer = []
    
    for log in record:
        splited_log = log.split()
        command, uid = splited_log[0], splited_log[1]
        if command == "Enter":
            answer.append(f"{uid_name_map[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{uid_name_map[uid]}님이 나갔습니다.")
            
    
    return answer