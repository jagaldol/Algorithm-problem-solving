N = int(input())

number_left_big_list = list(map(int, input().split()))

result = [0 for _ in number_left_big_list]

for i in range(len(number_left_big_list)):
    number_left_big = number_left_big_list[i]
    number_left = number_left_big
    j = 0
    while j <= number_left :
        if result[j]:
            number_left += 1
        j += 1
        
    
    result[number_left] = i+1
print(' '.join(map(str, result)))