import sys

T = int(input())
lst = []
for i in range(T):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()
for i in range(T):
    print(lst[i])
