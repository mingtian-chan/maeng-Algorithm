import math

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    ret = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))

    print(ret)
