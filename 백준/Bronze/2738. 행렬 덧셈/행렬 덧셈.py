a, b = map(int, input().split())
lst1 = []
lst2 = []
for i in range(a):
    lst1.append(list(map(int, input().split())))
for i in range(a):
    lst2.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
        print(lst1[i][j]+ lst2[i][j], end=" ")
    print("")