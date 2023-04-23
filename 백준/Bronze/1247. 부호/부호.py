import sys

for _ in range(3):
    T = int(sys.stdin.readline())
    sum = 0

    for i in range(T):
        sum += int(sys.stdin.readline())
    
    if sum > 0:
        print("+")
    elif sum == 0:
        print("0")
    else:
        print("-")
    