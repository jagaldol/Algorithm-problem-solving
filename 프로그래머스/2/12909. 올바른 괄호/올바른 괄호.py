def solution(s):
    balance = 0
    for c in s:
        balance += 1 if c == "(" else -1
        
        if balance < 0:
            return False
    
    return balance == 0