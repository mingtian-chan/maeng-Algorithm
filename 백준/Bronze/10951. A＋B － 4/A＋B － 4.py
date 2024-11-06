import sys

lines = sys.stdin.readlines()
for i in lines:
    i.rstrip()
    a,b=  map(int, i.split())
    print(a+b)
