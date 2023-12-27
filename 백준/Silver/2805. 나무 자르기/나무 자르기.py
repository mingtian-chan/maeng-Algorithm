N, M = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = max(lst)

ans = 0
while left < right:
    total = 0
    mid = (left + right) // 2
    for i in lst:
        total += max(0, i - mid)
    if total >= M:
        ans = mid
        left = mid + 1

    else:
        right = mid

print(ans)

