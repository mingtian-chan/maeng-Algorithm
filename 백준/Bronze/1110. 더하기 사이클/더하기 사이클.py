cycle = 0
a = int(input())
b = a//10
c = a % 10
while (True):
    tmp = b
    b = c
    c = (tmp + b)%10
    cycle += 1
    if a == 10*b+c:
        break
print(cycle)
