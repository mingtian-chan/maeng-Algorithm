n, x, y = map(int,input().split())
if 0.5 * n > x:
    x = n - x

if 0.5 * n > y:
    y = n - y

print(4 * x * y)
