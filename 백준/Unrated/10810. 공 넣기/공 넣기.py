N, M = map(int,input().split())
lst = [0]*N

for _ in range(M):
    i, j, k = map(int,input().split())
    for a in range(i-1, j):
        lst[a] = k

for i in lst:
    print(i, end=" ")