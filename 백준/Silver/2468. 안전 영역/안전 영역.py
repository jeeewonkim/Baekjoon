import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
big  = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    big = max(max(graph[i]), big)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def search(visited,start):
    queue = deque()
    queue.append(start)
    visited[x][y] = 1
    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            nx = now_x+dx[i]
            ny = now_y+ dy[i]
            if 0 <= nx < N and 0 <=ny <N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
max_res = 0
for i in range(0, big+1):
    res = 0
    visited = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if graph[x][y] <= i:
                visited[x][y] = 1
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                res +=1
                search(visited,[x,y])

    max_res = max(res, max_res)

print(max_res)