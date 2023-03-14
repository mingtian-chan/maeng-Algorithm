T = int(input())
for _ in range(T):
    s = input()
    cnt = 0
    for i in s:
        if i == "D":
            break
        cnt += 1
    print(cnt)
