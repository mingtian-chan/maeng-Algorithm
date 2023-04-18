a, b = map(int,input().split())
# 0이 아닐 때 까지 반복해서 0 0 이면 끝
while a + b != 0:
    print(a+b)
    a, b = map(int,input().split())