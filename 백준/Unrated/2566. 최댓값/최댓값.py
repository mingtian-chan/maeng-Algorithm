maxint = -1
idx = [-1, -1]
for i in range(9):
    lst = list(map(int,input().split()))
    for j in range(9):
        if lst[j] > maxint:
            idx[0:2] = [i+1,j+1]
            maxint = lst[j]
print(maxint)
print(idx[0], idx[1])