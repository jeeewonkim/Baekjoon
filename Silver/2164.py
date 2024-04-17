from collections import deque
import sys

n = int(sys.stdin.readline())
 
card = deque(i for i in range(1,n+1))


result = 0
while True:
    if len(card) ==1:
        result = card[0]
        break
    else:
        card.popleft()
        card.append(card.popleft())
        
print(result)