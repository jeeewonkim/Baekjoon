#미로탐색

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        #네 방향으로 확인하기 위한
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))

    return miro[n-1][m-1]

print(bfs(0,0))

