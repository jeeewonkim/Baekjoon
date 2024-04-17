#유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
#M : 가로길이, N: 세로길이, K: 배추의 위치
dx = [0,0,1,-1]
dy = [1,-1,0,0]
worms = 0
def bfs(y,x):
    global worms
    worms += 1
    field[y][x] +=1
    queue = deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx< 0 or ny <0 or nx>= M or ny>= N:
                continue
            if field[ny][nx] == 0:
                continue
            if field[ny][nx] == 1:
                queue.append((ny,nx))
                field[ny][nx] = field[y][x]+1
    return


#배추 위치 입력 받기
for _ in range(T):
    worms = 0
    M, N, K = map(int, input().split())
    field = [[False] * M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        field[y][x] = True

    for ly in range(N):
        for lx in range(M):
            if field[ly][lx] == 1:
                bfs(ly,lx)
    print(worms)


#깊이 우선 탐색

#유기농 배추

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        dfs(nx, ny)

for _ in range(T):
    count = 0
    m, n , k = map(int,input().split())
    graph = [[0] * (m) for _ in range(n)]

    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs(x,y)
                count +=1
    print(count)
