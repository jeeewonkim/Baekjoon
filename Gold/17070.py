import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,1] #가로, 세로 , 대각선
dy = [1,0,1]
result = 0
def pipe(x,y,d):
    global result
    if x == n-1 and y == n-1:
        return

    for i in range(3):
        if (d == 0 and i == 1) or (d ==1 and i == 0):
            continue
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1:
            if i == 2 and (graph[nx - 1][ny] == 1 or graph[nx][ny - 1] == 1):
                continue
            graph[nx][ny] -=1
            pipe(nx,ny,i)

if graph[n-1][n-1] == 1:
    print(0)
    exit(0)
else:
    pipe(0,1,0)
    print(abs(graph[n-1][n-1]))