import sys

lst = sys.stdin.readlines()
for i in lst:
    N, S = map(int, i.strip().split())
    print(S // (N + 1))
