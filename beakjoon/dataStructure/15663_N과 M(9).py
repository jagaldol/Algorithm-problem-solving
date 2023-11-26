N, M = list(map(int, input().split()))

input_list = list(map(int, input().split()))
numbers = []


def dfs(output, count):
    if len(output) == M:
        print(*output)
        return
    for i in numbers:
        if count[i] == 0:
            continue
        output.append(i)
        count[i] -= 1
        dfs(output, count)
        output.pop()
        count[i] += 1


def main():
    input_list.sort()

    count = {}

    for i in range(N):
        if i > 0 and input_list[i] == input_list[i - 1]:
            count[input_list[i]] += 1
            continue
        numbers.append(input_list[i])
        count[input_list[i]] = 1

    dfs([], count)


main()
