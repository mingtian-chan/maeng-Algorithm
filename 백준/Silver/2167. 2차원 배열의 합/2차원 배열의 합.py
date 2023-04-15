import sys
N,M = map(int,sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

T = int(sys.stdin.readline())
for _ in range(T):
    ax, ay, bx, by = map(int,sys.stdin.readline().split())
    sum = 0
    for i in range(ax,bx+1):
        for j in range(ay,by+1):
                sum += lst[i-1][j-1] 
    print(sum)