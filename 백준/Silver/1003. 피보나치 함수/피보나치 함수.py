T = int(input())

lst = [0, 1]  # 피보나치를 저장하는 리스트

for _ in range(T):
    i = int(input()) 
    

    while len(lst) < i+1 :
        lst.append(lst[len(lst)-2]+lst[len(lst)-1])
    
    if i == 0:
        print(1, 0)
    else:
        print(lst[i-1], lst[i])

