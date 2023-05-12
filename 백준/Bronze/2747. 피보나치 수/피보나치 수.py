def fibo(n):
    prev = 0
    curr = 1
    
    if n < 2:
        return n
    
    for i in range(n-1):
        tmp = curr
        curr += prev
        prev = tmp
    
    return curr

T = int(input())
print(fibo(T))