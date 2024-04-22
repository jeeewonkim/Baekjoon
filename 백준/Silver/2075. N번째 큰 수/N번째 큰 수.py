import sys,heapq
input = sys.stdin.readline
heap = []
N = int(input())
for i in range(N):
    for num in list(map(int, input().split())):
        if len(heap) < N:
            heapq.heappush(heap,num)
        else:
            if heap[0] < num:
                a = heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])