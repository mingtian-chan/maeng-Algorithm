N, W, H= map(int,input().split())
for _ in range(N):
    i = int(input())
    if i**2 > (W**2 + H**2):
        print("NE")
    else:
        print("DA")