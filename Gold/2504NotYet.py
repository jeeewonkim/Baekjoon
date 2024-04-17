import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []
tmp = 1
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        tmp *= 2
    elif s[i] == '[':
        stack.append('[')
        tmp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if s[i-1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i-1] == '[':
            ans +=tmp
        tmp//=3
        stack.pop()


print(ans if not stack else 0)


