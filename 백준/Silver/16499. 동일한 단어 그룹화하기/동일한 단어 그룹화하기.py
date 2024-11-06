n = int(input())
lst = []
for _ in range(n):
    a = input()
    a_lst = list(a)
    a_lst.sort()
    # print(a_lst)
    if (a_lst) not in lst:
        lst.append(a_lst)
print(len(lst))

# 주의 할 점 : 
# set으로 처리할 시 각 단어의 숫자가 체크되지 않아
# abbb 와 abab는 같은 그룹으로 친다. 