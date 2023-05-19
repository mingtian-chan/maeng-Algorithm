ans = []
for i in range(5):
    s = input()
    if "FBI" in s:
        ans.append(i)
    
if len(ans):
    for i in ans:
        print(i+1, end=" ")
else:
    print("HE GOT AWAY!")