import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0] *(n+1) for _ in range(n+1)]
graph[1][1] = 2

for i in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
op = [[] for _ in range(l)]
for i in range(l):
    op[i]  = list(map(str, input().split()))
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir = 0
snake = deque()
snake.append([1,1])
time = 0
x, y = 1,1
idx = 0
while True:
    x += dx[dir]
    y += dy[dir]
    time +=1
    if x<1 or x>n or y<1 or y>n or graph[x][y] == 2:
        break
    else:
        if time == int(op[idx][0]):
            if op[idx][1] == 'D':
                dir = (dir + 1) % 4
            elif op[idx][1] == 'L':
                dir = (dir + 3) % 4
            if idx < l-1 : idx +=1

        if graph[x][y]  == 0:
            tail_x, tail_y = snake.popleft()
            graph[tail_x][tail_y]  = 0

        graph[x][y] = 2
        snake.append([x,y])

print(time)

