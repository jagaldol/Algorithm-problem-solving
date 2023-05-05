from collections import deque

N, M = map(int, input().split())
quest = map(int, input().split())

queue = deque([i for i in range(1, N+1)])

count = 0

for q in quest:
    while True:
        if queue[0] == q:
            queue.popleft()
        else:
            if queue.index(q) < len(queue)/2:
                while queue[0] != q:
                    queue.append(queue.popleft())
                    count += 1
            else:
                while queue[0] != q:
                    queue.appendleft(queue.pop())
                    count += 1

print(count)