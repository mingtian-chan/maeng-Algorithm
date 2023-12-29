INF = int(1e9)


n, m = map(int, input().split())


graph = [[INF] * (n+1) for i in range(n+1)]

# 그래프 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 거리의 최솟값 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


lst = [graph[i][i] for i in range(1,n+1)]

if min(lst) == INF:
    print(-1)
else:
    print(min(lst))

