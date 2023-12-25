import heapq

T = int(input())
heap = []

for idx in range(T):
    a, b = input().split()
    a = int(a)
    # heappush하니까 리스트를 넣으면 lst[0] lst[1] lst[2]에 대해서 heap이 넣음
    # 리스트의 모든 요소에 대해서 정렬된 힙이 만들어짐.
    # 그래서 idx를 넣어주면 넣은 순서대로 출력가능
    heapq.heappush(heap, [a, idx, b])

while heap:
    a = heapq.heappop(heap)

    print(a[0], a[2]) 


