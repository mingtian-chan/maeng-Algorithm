while True:
    a = list(map(int,input().split()))
    if len(a) == 1:
        break
    branch = 1
    for i in range(1,2*a[0]+1):
        if i % 2 == 1:
            branch *= a[i]
            continue
        branch -= a[i]
    print(branch)
