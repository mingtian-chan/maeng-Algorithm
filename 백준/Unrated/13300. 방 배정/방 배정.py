cnt = 0
T, r = map(int,input().split())
arr = [[r-1 for i in range(7)] for j in range(2)]
for i in range(T):
    a, b = map(int,input().split())
    arr[a][b] += 1
    if arr[a][b] >= r:
        cnt += 1
        arr[a][b] = 0

print(cnt)