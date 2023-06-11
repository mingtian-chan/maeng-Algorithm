def greedy(money,cnt):
    lst = [500,100,50,10,5,1]

    for i in lst:
        cnt += (money//i)
        money %= i
    
    return cnt


money = 1000 - int(input())
print(greedy(money,0))