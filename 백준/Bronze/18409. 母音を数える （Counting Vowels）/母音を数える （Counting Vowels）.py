lst = ["a","e","i","o","u"]
T = int(input())
s = input()
cnt = 0
for i in s:
    if i in lst:
        cnt+= 1

print(cnt)