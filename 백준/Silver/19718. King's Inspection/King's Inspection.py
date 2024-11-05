a = int(input())
b = int(input())
c = int(input())
lst = [a,b,c]
lst.sort()
cnt = lst[1] + lst[2] - 2*lst[0]
print(cnt)