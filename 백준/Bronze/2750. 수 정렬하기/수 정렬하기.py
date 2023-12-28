import heapq
import sys

T = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(T):
    i = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, i)

for i in range(T):
    print(heapq.heappop(heap))



