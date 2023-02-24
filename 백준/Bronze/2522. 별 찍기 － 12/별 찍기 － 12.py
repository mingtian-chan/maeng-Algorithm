T = int(input())
for i in range(1,T+1):
    print(" "*(T-i)+"*"*i)
for i in range(1,T):
    print(" "*i+"*"*(T-i))