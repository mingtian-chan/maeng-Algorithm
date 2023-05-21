from collections import deque

N = int(input())

pizza =  list(map(int,input().split()))

ans = [0 for i in range(N)]

queue = deque()

for i in range(N):
    queue.append([i,0])

count = 0
while queue:
    num, get = queue.popleft() # 사람번호, 받은 피자수 
    count += 1

    get += 1

    if pizza[num] == get: # 배부르는 개수랑 받은 개수가 같으면, 
        ans[num] = count # ans 에 언제 배부르게 되었는지 적는다.

    else:
        queue.append([num, get]) # 배가 부르지 않다면 큐의 마지막에 다시 넣는다.


ans = map(str,ans)
print(" ".join(ans))

