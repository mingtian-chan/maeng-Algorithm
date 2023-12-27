


T = int(input())
lst = list(map(int, input().split()))
M = int(input())

left = 0
right = max(lst)

while left <= right:
    budget = 0
    mid = (left + right) // 2
    for i in lst:
        budget += min(i, mid)
    # print("__________________")
    # print("left :", left)
    # print("right :", right)
    # print("M :", M)
    # print("budget :", budget)

    if budget <= M:
        left = mid + 1

    else:
        right = mid - 1

print(right)

