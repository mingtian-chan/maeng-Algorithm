import sys

N, K = map(int, input().split())
# N : 계단 수, F : 걸음 수
dp = [float("INF") for _ in range(N+1)]

dp[0] = 0

for i in range(1, N+1):

    # 계단 1 칸 올라가기
    dp[i] = min(dp[i], dp[i-1]+1)

    # 순간이동
    if (i+i//2) <= N:
        dp[i+ i//2] = min(dp[i+ i//2], dp[i]+1)

if dp[N] <= K:
    print("minigimbob")
else:
    print("water")