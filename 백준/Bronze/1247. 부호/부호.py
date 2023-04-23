import sys

# sys.readline()으로 입출력 받는 시간 줄여서 해결

## pypy3쓰면 시간 더 줄일 수 있음.
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
    