import sys
a, b = sys.stdin.readline().split()

a_hap = 0
b_hap = 0
for i in a:
    a_hap += int(i)
for j in b:
    b_hap += int(j)

print(a_hap * b_hap)