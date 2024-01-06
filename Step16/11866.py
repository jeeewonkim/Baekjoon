from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

queue = deque(i for i in range(1,n+1))
result =[]
while len(queue)!=0:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    
result_print = "<" + ", ".join(map(str,result))+">" 

print(result_print)