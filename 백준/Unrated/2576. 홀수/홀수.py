sum = 0
min = 101
for _ in range(7):
    i = int(input())
    if i % 2 == 1:
        sum += i
        if i < min:
            min = i

if (sum != 0) and (i != 101):
    print(sum)
    print(min)
else:
    print(-1)