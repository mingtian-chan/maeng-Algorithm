T = int(input())
s = len(input())
if s == 7.5*T:
    print("bigdata? security!")
elif s > 7.5*T:
    print("security!")
else:
    print("bigdata?")