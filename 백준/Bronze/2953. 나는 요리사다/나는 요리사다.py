max = -1
idx  = -1
for i in range(5):
    lst = list(map(int,input().split()))

    if max < sum(lst):
        max = sum(lst)
        idx = i+1
    
print(idx, max)

    

