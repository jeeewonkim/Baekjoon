from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    c = sys.stdin.readline().split()
    if c[0] == '1' :
        deq.appendleft(c[1])
    if c[0] == '2' :
        deq.append(c[1])
    if c[0] == '3':    
        print(deq.popleft() if deq else -1)
    if c[0] == '4':
        print(deq.pop() if deq else -1)
    if c[0] == '5':
        print(len(deq))
    if c[0] == '6':
        print(0 if deq else 1)
    if c[0] == '7' :
        print(deq[0] if deq else -1)
    if c[0] == '8' :
        print(deq[-1] if deq else -1)
