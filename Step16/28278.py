import sys
stack= []

    
n = int(sys.stdin.readline())
for i in range(n):
    c = sys.stdin.readline().split()
    
    if c[0] == '1':
        stack.append(c[1])
    if c[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if c[0] == '3':
        print(len(stack))
    if c[0] == '4':
        print(1 if not stack else 0)
    if c[0] == '5':
        print(-1 if not stack else (stack[-1]))
