T = int(input())
lst = []
for _ in range(T):
    a, b = map(int,input().split())

    lst.append((a,b))

lst.sort()
lst.sort(key= lambda x:x[1])
for i in lst:
    print(i[0], i[1])