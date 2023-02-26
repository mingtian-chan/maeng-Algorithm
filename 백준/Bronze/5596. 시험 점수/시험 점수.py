lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
sum1 = 0
sum2 = 0

for i in lst1:
    sum1 += i

for i in lst2:
    sum2 += i

print(max(sum1, sum2))