import sys
input= sys.stdin.readline

s = input().strip()
isIn = False
stack = []
result = ''
for i in range(len(s)):
    if s[i] == '<':
        isIn = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(s[i])

    if s[i] == '>':
        isIn = False
        for _ in range(len(stack)):
            result += stack.pop(0)
    if s[i] == ' ' and isIn == False:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
if stack :
    while stack:
        result += stack.pop()
print(result)
