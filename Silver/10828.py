#스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    mention = input().strip().replace(" ","")
    if mention[0:4] == 'push':
        stack.append(int(mention[4:]))
    elif mention[0:3] == 'top':
        print(stack[-1]) if stack else print(-1)
    elif mention[0:4] == 'size':
        print(len(stack))
    elif mention[0:5] == 'empty':
        print(0 if stack else 1)
    elif mention[0:3] == 'pop':
        print(stack.pop()) if stack else print(-1)




    # if mention[0:3] =='push':
    #     print(mention)