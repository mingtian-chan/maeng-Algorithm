
n = int(input())

mat = [[-1 for i in range(n)] for j in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        mat[i][j] = int(s[j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if mat[y][x] == 1:
        global cnt
        cnt += 1
        mat[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

ans = []
cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(j,i):
            ans.append(cnt)
            result += 1
            cnt = 0
ans.sort()
print(result)
for i in ans:
    print(i)