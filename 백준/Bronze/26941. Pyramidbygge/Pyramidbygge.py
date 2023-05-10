T = int(input())
i = 1
total = 1
while(total <= T):
    total += (2*i+1)**2
    i += 1
print(i-1)