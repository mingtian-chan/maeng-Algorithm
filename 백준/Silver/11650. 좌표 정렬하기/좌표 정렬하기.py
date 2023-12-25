T = int(input())
lst = []
for _ in range(T):
    a, b = map(int,input().split())
    
    lst.append((a,b))
    
lst.sort(key= lambda x:x[1])
lst.sort()
for i in lst:
    print(i[0], i[1])