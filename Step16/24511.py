import sys
from collections import deque
# 자료구조의 개수
n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))
#삽입할 수열의 길이
m = int(sys.stdin.readline())

c= list(map(int, sys.stdin.readline().split()))

queue = deque()
for j in range(n): 
     if a[j] == 0 :
         queue.appendleft(b[j])
            
            
for i in range(m):
    queue.append(c[i])
    print(queue.popleft(), end = " ")
    
            
    
