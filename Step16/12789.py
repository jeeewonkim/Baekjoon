# 처음엔 space도 queue로 두고 
# line속에서 찾을 수 있는 문자열은 전부 찾은 다음에
# queue속에서 해결하면 된다고 생각했는데
# space 에 해당 값이 있으면 먼저 빼줘야된다는 생각을 못함

import sys
from collections import deque
n = int(sys.stdin.readline())

line = deque(map(int,input().split()))

space = []

turn = 1
while turn <= n:
    #li = line.popleft()
    if line and line[0] == turn:
        line.popleft()
        turn +=1
    elif space and space[-1] == turn:
        space.pop()
        turn +=1
    else:
        if not line:
            break
        else:
            space.append(line.popleft())
            
if turn > n:
    print('Nice')
else:
    print('Sad')
# is_nice = True
# if space:
#     for first, second in zip(space[:-1], space[1:]):
#         if second - first != 1:
#             is_nice = False
#             break
        
# print(is_nice)
        
# print("Nice" if is_nice else "Sad")
    # max_value = max(space)
    # turn = min(space)
    # while space:
    #     while turn < max_value +1:
    #         if space.popleft() != turn:
    #             print("Sad")
    #             break
    #         else:
    #             turn +=1
    # print("Nice")
            

# while line:
#     li = line.popleft()
#     if li == 1:
#         continue
#     else :
#         space.appendleft(li)

# i = 2
# p = "Sad"
# while space:
#     while i < n+1:
#         if space.popleft() != i:
#             p = "Sad"
#             break
#         else:
#             i+=1
#             p = "Nice"
        
# print(p)        



# import sys

# n = int(sys.stdin.readline())

# line = list(map(int, input().split()))

# space = []

# for i in range(1,n+1):
#     for li in range(len(line)):
#         if line[li] == i :
#             break
#         else:
#             space.append(line.pop(li))

# for i in range(n):
    
# print(space)