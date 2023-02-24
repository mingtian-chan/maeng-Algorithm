T = int(input())
for i in range(1,T):
    print((i)*"*"+(2*(T-i))*" "+(i)*"*")

for i in range(T):
    print((T-i)*"*"+(2*i)*" "+(T-i)*"*")
