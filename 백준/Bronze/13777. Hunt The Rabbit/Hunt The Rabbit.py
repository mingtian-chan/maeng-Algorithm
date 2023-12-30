target = int(input())


while target:
    left = 1
    right = 50

    while left <= right:
        mid = (left + right) // 2
        print(mid, end = " ")

        if mid == target:
            print()
            break

        if mid < target:
            left = mid + 1
            continue

        else:
            right = mid - 1

    target = int(input())

