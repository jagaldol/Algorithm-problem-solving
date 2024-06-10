checked = []
answer = set()

def match(user, banned):
    if len(user) != len(banned): return False
    
    for i in range(len(user)):
        if banned[i] == "*": continue
        if banned[i] != user[i]: return False
    return True
        
        

def bt(user_id, banned_id, current):
    if current == len(banned_id):
        global answer
        answer.add("".join([str(i) for i, v in enumerate(checked) if v]))
        return
        
    for idx, user in enumerate(user_id):
        if checked[idx]: continue
        if match(user, banned_id[current]):
            checked[idx] = True
            bt(user_id, banned_id, current+1)
            checked[idx] = False

def solution(user_id, banned_id):
    global checked
    checked = [False] * len(user_id)
    bt(user_id, banned_id, 0)
    
    return len(answer)