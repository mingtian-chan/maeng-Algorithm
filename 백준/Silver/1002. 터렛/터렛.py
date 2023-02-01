T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    # 두 원 사이 거리
    r = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # 작은 원의 직경
    smaller = min(r1, r2)
    # 큰 원의 직경 
    bigger = max(r1, r2)

    # 두 원이 일치한다.
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    
    # 밖에서 두 원이 만나지 않는다
    elif  r > smaller + bigger:
        print(0)
    
    # 한 원이 다른원을 포함하면서, 만나지 않는다.
    elif bigger > smaller + r:
        print(0)

    # 두 원이 한 점에서 만난다 ( 밖에서든 안에서든 )
    elif r == bigger + smaller or bigger == r + smaller:
        print(1)
    
    # 두 점에서 만난다
    else:
        print(2)