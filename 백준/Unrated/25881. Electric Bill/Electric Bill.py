a, b = map(int, input().split())
T = int(input())
for _ in range(T):
    i = int(input())
    if i > 1000:
        print(i, 1000*a+ (i-1000)*b)
    else:
        print(i, i*a)
