
N = int(input())

for _ in range(N):
    lst = []
    money = 5000000
    i = int(input())
    while i:
        lst.append(i)
        i = int(input())

    lst.sort(reverse= True)
    cost = 0
    for i in range(len(lst)):
        cost += lst[i]**(i+1)*2
    if cost <= money:
        print(cost)
    else:
        print("Too expensive")