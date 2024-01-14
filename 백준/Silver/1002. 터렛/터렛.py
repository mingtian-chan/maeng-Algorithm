import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # dist1 = 두 점의 직선 거리 (두 원의 중심간 거리)
    dist1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # dist2 = 두 원의 반지름의 합
    dist2 = abs(r1+r2)

    # dist3 = 두 원의 반지름의 차
    dist3 = abs(r1-r2)

    # 두 원이 같을 때 ( 무한대 -> -1출력)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    # 두 원이 서로 안 만날 때
    elif dist1 > dist2 or dist1 < dist3:
        print(0)

    # 한 점에서 만날 때
    elif dist1 == dist2 or dist3 == dist1:
        print(1)

    # 두 점에서 만날 때
    else:
        print(2)




