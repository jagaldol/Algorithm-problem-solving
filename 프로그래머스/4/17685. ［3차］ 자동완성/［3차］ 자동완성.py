def compare(A, B):
    count = 0
    for a, b in zip(A, B):
        if a != b:
            break
        count += 1
    
    return count
    

def solution(words):
    words.sort()
    
    answer = 0
    
    for i in range(len(words)):
        if i == 0:
            length = compare(words[i], words[i + 1])
        elif i == len(words) - 1:
            length = compare(words[len(words) - 2], words[len(words) - 1])
        else:
            length = max(compare(words[i - 1], words[i]), compare(words[i], words[i + 1]))
        answer += length + (1 if length < len(words[i]) else 0)
            
    return answer