
k, n = map(int, input().split())
lst = []

for i in range(k):
    lst.append(int(input()))

left = 1
right = max(lst)

mid = (left + right) // 2
while left <= right:

    cnt = 0
    for i in lst:
        cnt += i // mid
    # print("-----------------------")
    # print("left :", left)
    # print("right :", right)
    # print("mid :", mid)
    # print("cnt :", cnt)

    if cnt >= n:  # 더 길게 잘라도 돼
        left = mid + 1
        mid = (left + right) // 2

    else:
        right = mid - 1
        mid = (left + right) // 2

print(mid)