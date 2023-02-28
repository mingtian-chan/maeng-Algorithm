T = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in lst:
    if T == i:
        ans += 1

print(ans)