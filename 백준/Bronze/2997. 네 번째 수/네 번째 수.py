lst = list(map(int, input().split()))
# 만약에 a b c 가 서로 등차수열인 경우
lst.sort()
if lst[1]*2 == lst[0] + lst[2]:
    # 앞의 등차수열값이 나와
    print(lst[0]*2-lst[1])

# 등차수열이 아닌 경우 : a b () c 이거나, a () b c 인 경우
else:
    print(lst[0]+lst[2]-lst[1])
