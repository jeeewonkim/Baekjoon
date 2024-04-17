import sys, heapq
N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    i = int(sys.stdin.readline().strip())
    
    if i == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    
        
    else:
        heapq.heappush(heap, (abs(i) , i))