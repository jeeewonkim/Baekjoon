import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = list(input().strip())
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        cnt +=1
print(cnt)
