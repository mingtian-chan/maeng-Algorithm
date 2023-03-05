T = int(input())
for i in range(1,T+1):
    print(i, end=" ")
    if i % 6 == 0 and i != T:
        print("Go!", end= " ")

print("Go!")