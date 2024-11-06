s = input()
lst = []
for i in s:
    if i.isupper():
        lst.append(i.lower())
    else:
        lst.append(i.upper())
print("".join(lst))