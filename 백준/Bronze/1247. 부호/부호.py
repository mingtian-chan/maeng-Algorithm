for _ in range(3):
    T = int(input())
    sum = 0

    for i in range(T):
        sum += int(input())
    
    if sum > 0:
        print("+")
    elif sum == 0:
        print("0")
    else:
        print("-")
    