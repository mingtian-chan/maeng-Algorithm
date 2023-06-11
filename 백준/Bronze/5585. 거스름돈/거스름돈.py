def greedy(i,cnt):
    if i >= 500:
        return greedy(i-500,cnt+1)
    if i >= 100:
        return greedy(i-100,cnt+1)
    if i >= 50:
        return greedy(i-50,cnt+1)
    if i >= 10:
        return greedy(i-10,cnt+1)
    if i >= 5:
        return greedy(i-5,cnt+1)
    if i >= 1:
        return greedy(i-1,cnt+1)
    else:
        return cnt



i = 1000 - int(input())
print(greedy(i,0))