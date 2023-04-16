T = int(input())
for _ in range(T):
    s = input()
    prev = " "
    result = ""
    for i in s:
        if prev != i:
            result += i
            prev = i
    print(result)