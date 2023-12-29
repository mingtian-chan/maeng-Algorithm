import heapq
INF = int(1e9)


# N is the number of Nodes, M is the number of Edges
# N starts at 1
N, M = map(int, input().split())
start = int(input())

graph = [[] for i in range(N + 1)]
dist = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra_pq(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    for d in dist[1:]:
        if d == INF:
            print("INF")
        else:
            print(d)


dijkstra_pq(start)