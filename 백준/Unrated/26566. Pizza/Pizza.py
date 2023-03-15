import math
T = int(input())
for _ in range(T):
    a1, p1 = map(int,input().split())
    r1, p2 = map(int,input().split())
    a2 = r1**2*math.pi
    if p1/a1 > p2/a2:
        print("Whole pizza")
    else:
        print("Slice of pizza")