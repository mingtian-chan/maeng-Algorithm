T = int(input())
for idx in range(1,T+1):
    s = []
    couple_lst = [("u","d"),("d","u"),("l","r"),("r","l")]
    r = input()

    for i in r:
        # print("stack: ",s)
        if len(s) == 0:
            s.append(i)
            # print("blank : append : ", i)
            continue
        j = s[-1]

        if (i,j) in couple_lst:
            s.pop()
            # print("couple : ",i, j)
            continue

        s.append(i)
    
    print("Data Set %d:" %idx)
    print("No" if len(s) else "Yes")    
    print()
