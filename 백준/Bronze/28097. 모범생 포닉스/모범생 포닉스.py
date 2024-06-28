n = int(input())
lst = list(map(int, input().split()))
print((sum(lst) + (n-1) * 8 )// 24, (sum(lst) + (n-1) * 8) % 24)
