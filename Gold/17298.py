import sys
sys = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
ans = [-1] *(n)
stack = [0]
for i in range(1,n):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)
print(*ans)
