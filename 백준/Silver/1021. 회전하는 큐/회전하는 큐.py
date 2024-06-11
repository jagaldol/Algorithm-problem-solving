from collections import deque

N, M = map(int, input().split())
quest = map(int, input().split())

queue = deque([i for i in range(1, N+1)])

count = 0

for q in quest:  # 뽑아내려는 수의 위치 하나씩 반복문 돌리기
    while True:     # 뽑을 때까지 계속 돌리기
        if queue[0] == q:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            queue.popleft()
            break
        else:
            if queue.index(q) < len(queue)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while queue[0] != q:   # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    queue.append(queue.popleft())  
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while queue[0] != q:
                    queue.appendleft(queue.pop())  
                    count += 1
print(count)