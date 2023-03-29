N = int(input())
flag = 0
for i in range(1,N+1):
    tmp = i
    ans = 0
    ans += tmp
    while tmp > 0:
        ans += (tmp % 10)
        tmp = tmp // 10
    if ans == N:
        flag = i
        break
print(flag)

