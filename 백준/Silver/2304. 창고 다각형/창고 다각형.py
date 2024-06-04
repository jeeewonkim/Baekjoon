import sys
input = sys.stdin.readline

n = int(input())
graph = []
height = [0] * 1001
max_h, max_idx = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    graph.append([x,y])
    height[x] = y
    if max_h < y:
        max_h, max_idx = y,x

graph = sorted(graph, key = lambda x: x[0])


d = 0
#왼쪽
width = height[max_idx]
stack = []
for i in range(max_idx):
    if not stack:
        stack.append(height[i])
    elif stack and stack[-1] < height[i]:
        stack.pop()
        stack.append(height[i])
    width += stack[-1]

stack = []
for j in range(graph[-1][0] , max_idx, -1):
    if not stack:
        stack.append(height[j])
    elif stack and stack[-1] < height[j]:
        stack.pop()
        stack.append(height[j])
    width += stack[-1]
print(width)