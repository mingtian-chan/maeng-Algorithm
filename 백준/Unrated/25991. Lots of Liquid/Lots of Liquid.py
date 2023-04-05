
T = int(input())
a = 0
lst = list(map(float,input().split()))
for i in lst:
    a += i**3

print(a**(1/3))