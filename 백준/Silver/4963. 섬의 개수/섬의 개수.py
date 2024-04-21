import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0,1,1,-1,-1] #상하 좌우 #대왼상 #대우상 #대왼하 #대우하
dy = [0,0,-1,1,-1,1,-1,1]
def bfs(graph, start,w, h):
    q = deque([start])
    while q:
        now_x, now_y = q.popleft()
        for i in range(8):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    elif w == 1 and h == 1:
        print(int(input()))
        continue
    res = 0

    graph = list(list(map(int, input().split())) for _ in range(h))
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                bfs(graph, [x,y], w, h)
                res +=1
    print(res)