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
