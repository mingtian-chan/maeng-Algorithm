N = int(input())

lst = list(map(int, input().split()))

prev = -1
cnt = 0
for i in range(N):
    if lst[i] >= prev:
        cnt += 1
    prev = lst[i]
print(cnt)