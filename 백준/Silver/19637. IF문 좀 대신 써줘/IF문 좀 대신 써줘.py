import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

title = []
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    title.append((a, int(b)))

atk = []
for _ in range(m):
    tmp = int(sys.stdin.readline().rstrip())

    left, right = 0, n-1
    mid = (left+right)//2
    while left <= right:

        if tmp > title[mid][1]:
            left = mid+1
        else:
            right = mid-1
        mid = (left+right)//2
    mid = left
    print(title[mid][0])
