T = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst1.sort()
lst2.sort()
ans = 0

for i in range(T):
    ans += lst1[i] * lst2[T-i-1]

print(ans)
