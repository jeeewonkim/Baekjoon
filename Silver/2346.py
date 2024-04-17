from collections import deque
import sys
n = int(sys.stdin.readline())
balloon = deque(enumerate(map(int, input().split())))
result =[]

while balloon:
    idx, paper = balloon.popleft()
    result.append(idx+1)
    
    if paper > 0 :
        balloon.rotate(-(paper-1))
    elif paper < 0:
        balloon.rotate(-paper)

print(' '.join(map(str, result)))


# while balloon:
#     b = balloon[0]
#     result.append(balloon.popleft())

#     if b > 0:
#         for i in range(b-1):
#             balloon.append(balloon.popleft())
#     if b < 0 :
#         for i in range(abs(b)):
#             balloon.appendleft(balloon.pop())

#result.append(balloon[0])

#print(' '.join(map(str, result)))