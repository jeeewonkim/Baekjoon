import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []
stick = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])

    elif s[i] == ')':
        if s[i-1] == '(':
            stack.pop()
            stick += len(stack)

        else:
            stack.pop()
            stick +=1


print(stick)
