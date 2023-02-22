tot = 0
max_num = 0
for _ in range(10):
    o, i = map(int,input().split())
    tot = tot - o + i
    if tot > max_num:
        max_num = tot

print(max_num)