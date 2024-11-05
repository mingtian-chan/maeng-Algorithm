a,b,c = map(int, list(input().split()))
for i in range(a):
    H,W =input().split()
    if c == 0:
        b -= 1
        c += 1
        ans = "Y "
    else:
        if H == "Y":
            b -= 1
            c += 1
            ans = "Y "
        else:
            ans = "N "
    
    if b == 0:
        c -= 1
        b += 1
        ans += "Y"
    else:
        if W == "Y":
            c -= 1
            b += 1
            ans += "Y"
        else:
            ans += "N"
    print(ans)