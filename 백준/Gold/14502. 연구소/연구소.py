import sys, copy
input = sys.stdin.readline
from itertools import combinations
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
zero = []
virus = deque()
origin = 3
for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(m):
        if graph[i][j] == 0:
            zero.append([i,j])
        elif graph[i][j] == 2:
            virus.append([i,j])
            origin+=1
        elif graph[i][j] == 1:
            origin +=1
combi = list(combinations(zero, 3))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    cnt = 0
    q = copy.deepcopy(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                q.append([nx,ny])
                cnt +=1
    return cnt

result = 0

for i in combi:
    copy_graph = copy.deepcopy(graph)
    for j in range(3):
        copy_graph[i[j][0]][i[j][1]] = 1
    result = max(result, n*m-bfs()-origin)



print(result)