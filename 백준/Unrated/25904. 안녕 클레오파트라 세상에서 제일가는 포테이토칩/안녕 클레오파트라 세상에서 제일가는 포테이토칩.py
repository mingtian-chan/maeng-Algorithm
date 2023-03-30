N, tone = map(int,input().split())
lst = list(map(int,input().split()))
i = 0
while(True):
    if lst[i%N] < tone:
        print(i%N+1)
        break
    tone += 1
    i += 1
