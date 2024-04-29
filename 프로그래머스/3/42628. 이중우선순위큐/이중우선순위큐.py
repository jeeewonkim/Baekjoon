import heapq

def solution(operations):
    maxheap = []
    minheap = []
    length = 0
    for o in operations:
        if length == 0:
            maxheap = []
            minheap = []
        op, num = o.split(" ")
        if op == 'I':
            heapq.heappush(minheap,int(num))
            heapq.heappush(maxheap, -1*int(num))
            length +=1
        elif op == 'D':
            if length > 0:
                length -=1
                if int(num) < 0:
                    heapq.heappop(minheap)
                else:
                    heapq.heappop(maxheap)
        
    return [0,0] if length <= 0 else [-heapq.heappop(maxheap), heapq.heappop(minheap)]