k,w,m = map(int,input().split())
if k >= w:
    print(0)
else:
    print((w-k-1)//m + 1)