def magic2order(word):
    result = 0
    for c in word:
        result = result * 26 + ord(c) - ord('a') + 1
    return result

def order2magic(n):
    result = []
    while n > 0:
        mod = n % 26
        if result and result[-1] == 'z':
            mod -=1
        result.append(chr(mod + ord('a') - 1) if mod != 0 else 'z')
        n //= 26
    return "".join(reversed(result))

def solution(n, bans):
    sorted_bans = sorted(bans, key= lambda x: (len(x), x))
    for ban in sorted_bans:
        if magic2order(ban) <= n:
            n += 1
    return order2magic(n)