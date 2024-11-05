N, M = map(int, input().split())

lst1 = []
lst2 = []
    
for i in range(M):
    a, b = map(int, input().split())
    lst1.append(a)
    lst2.append(b)

# case 1 묶음으로만 사는 경우
# case 2 묶음 + 낱개로 사는 경우
# case 3 낱개로만 사는 경우
ans = min(
    ((N+5)//6)*min(lst1),
    (N//6) * min(lst1) + N%6 * min(lst2),
    N * min(lst2)
)
print(ans)