import sys
input = sys.stdin.readline

word = input().strip()
stack = []
cnt = 0
for w in word:
    if w == '(':
        stack.append(w)
    elif w == ')':
        if not stack:
            cnt +=1
        else:
            stack.pop()

print(cnt + len(stack))

