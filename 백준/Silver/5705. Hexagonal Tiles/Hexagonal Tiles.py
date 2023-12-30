memo = [1,2]

T = int(input())

def fibo(target):
    if len(memo) > target:
        return memo[target-1]

    if target <= 2:
        return target

    ret = fibo(target - 1) + fibo(target - 2)
    if ret not in memo:
        memo.append(ret)
    return ret
while T:
    print(fibo(T))
    T = int(input())
