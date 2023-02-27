T = int(input())
for i in range(T):
    print(" "*i+"*"*(2*(T-i)-1))
for i in range(2,T+1):
    print(" "*(T-i)+"*"*(i*2-1))

