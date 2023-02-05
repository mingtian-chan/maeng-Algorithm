T = int(input())

a = T // 300
T -= a * 300

b = T // 60
T -= b * 60

c = T // 10
T -= c * 10

if T != 0:
    print(-1)
else:
    print(a, b, c)