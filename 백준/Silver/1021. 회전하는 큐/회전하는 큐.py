from collections import deque

M, N = map(int, input().split())

lst = list(map(int, input().split()))
ans = 0
queue = deque(i for i in range(1,M+1))

for i in lst:
    idx = queue.index(i)
    if idx <= len(queue)/2:
        for _ in range(idx):
            a = queue.popleft()
            queue.append(a)
            ans += 1
        queue.popleft()
    else:
        for _ in range(len(queue)-idx):
            a = queue.pop()
            queue.appendleft(a)
            ans += 1
        queue.popleft()

print(ans)

