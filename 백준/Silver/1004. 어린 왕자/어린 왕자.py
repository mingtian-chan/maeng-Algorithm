T = int(input())
for _ in range(T):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int,input().split())
        
        m = min(((x1-cx)**2 + (y1-cy)**2)**0.5 ,((x2-cx)**2 + (y2-cy)**2)**0.5)
        M = max(((x1-cx)**2 + (y1-cy)**2)**0.5 ,((x2-cx)**2 + (y2-cy)**2)**0.5)
        if r > m and r < M:
            ans += 1

    print(ans)
