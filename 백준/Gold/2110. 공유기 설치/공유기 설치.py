
n, c = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))


def install_router(lst, C):
    lst.sort()

    lo = 1
    hi = lst[-1] - lst[0]
    min_gap = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 1
        cur = lst[0]
        for i in range(1, len(lst)):
            if lst[i] >= cur + mid:
                cur = lst[i]
                cnt += 1

        if cnt >= C:
            min_gap = mid
            lo = mid + 1

        else:
            hi = mid - 1

    return min_gap


print(install_router(l, c))
