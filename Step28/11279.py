#최대 힙

import sys , heapq
N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    i = int(sys.stdin.readline().strip())
    
    if i == 0 :
        print(-heapq.heappop(heap) if heap else 0)
        
    else:
        heapq.heappush(heap, -i)
        
    