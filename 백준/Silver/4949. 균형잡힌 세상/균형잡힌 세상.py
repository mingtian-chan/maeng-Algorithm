while (True):
    sentence = input()
    lst = []
    idx = 0
    if sentence == ".":
        break
    for i in sentence:
        if i == "]":
            if lst.count("[") == 0:
                print("no")
                idx = 1
                break  
            if lst.pop() == "(":
                print("no")
                idx = 1
                break

        if i == ")":
            if lst.count("(") == 0:
                print("no")
                idx = 1
                break
            if lst.pop() == "[":
                print("no")
                idx = 1
                break

        if i == "[":
            lst.append("[")
        if i == "(":
            lst.append("(")
    if idx == 0:
        if len(lst) == 0:
            print("yes")
        if (len(lst) != 0) :
            print("no")