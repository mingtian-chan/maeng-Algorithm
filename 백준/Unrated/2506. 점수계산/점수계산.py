T = int(input())
lst = list(map(int,input().split()))
ans = 0
cnt = 0
for i in lst:
    if i == 1:
        cnt += 1
        ans += cnt
        continue
    cnt = 0

print(ans)