import sys

T = int(input())

lst = sys.stdin.readlines()
lst = list(set(lst))
lst.sort()
lst.sort(key=lambda x: len(x))

for i in lst:
    print(i.rstrip())