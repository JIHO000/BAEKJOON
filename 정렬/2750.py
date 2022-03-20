import heapq
heap = []
n = int(input())
for _ in range(n):
    heapq.heappush(heap,int(input()))
for _ in range(n):
    print(heapq.heappop(heap))