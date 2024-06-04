import sys
input = sys.stdin.readline
n = int(input())
building = []

for _ in range(n):
    building.append(int(input()))
cnt = 0
stack = []
answer = [0] * n

for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    cnt += len(stack)-1
print(cnt)