import math

T = math.factorial(int(input()))
ans = 0
while (T % 10 == 0):
    ans += 1
    T = T // 10

print(ans)