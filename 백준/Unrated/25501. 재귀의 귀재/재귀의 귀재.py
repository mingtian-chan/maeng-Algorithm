def recursion(s, l, r,cnt):
    cnt += 1
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)

T = int(input())
for _ in range(T):
    i = input()
    ret, cnt = (isPalindrome(i,0))
    print(ret, cnt)
