import sys

str1 = '`1234567890-='
str2 = 'QWERTYUIOP[]\\'
str3 = 'ASDFGHJKL;\''
str4 = 'ZXCVBNM,./'

lines = sys.stdin.readlines()
for l in lines:
    output = ''
    for i in l:
        if i == ' ':
            output += i
            continue
        
        if i in str1:
            output += str1[str1.index(i)-1]
            continue
        if i in str2:
            output += str2[str2.index(i)-1]
            continue
        if i in str3:
            output += str3[str3.index(i)-1]
            continue
        if i in str4:
            output += str4[str4.index(i)-1]
            continue
        
    print(output)
