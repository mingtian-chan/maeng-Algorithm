T = int(input())

for i in range(T):
    c = int(input())
    # 쿼터
    print(c//25, end= " ")
    c = c % 25
    # 다임
    print(c//10, end= " ")
    c = c % 10
    # 니켈
    print(c//5, end= " ")
    c = c % 5
    # 페니 
    print(c)