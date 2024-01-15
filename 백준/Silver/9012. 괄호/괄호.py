T = int(input())

for _ in range(T):
    s = input()
    flag = 0 # 비정상종료시 1
    st = []
    for i in s:
        if i == "(":
            st.append("(")

        if i == ")":
            if len(st) == 0:
                print("NO")
                flag = 1
                break
            st.pop()

    if flag == 0:
        if len(st) != 0:
            print("NO")
            continue
            
        print("YES")

