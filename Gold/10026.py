# 적록색약
import copy
import sys

sys = sys.stdin.readline
from collections import deque

n = int(input())
RGB = ['R', 'G', 'B']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
grid = []

count = 0
count2 = 0

for i in range(n):
    grid.append(list(map(str, input().strip())))
copy_grid = copy.deepcopy(grid)


def bfs(x, y, rgb):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and copy_grid[nx][ny] == rgb:
                queue.append((nx, ny))
                copy_grid[nx][ny] = 'X'


for rgb in RGB:
    for x in range(n):
        for y in range(n):
            if copy_grid[x][y] == rgb:
                count += 1
                bfs(x, y, rgb)

for x in range(n):
    for y in range(n):
        if grid[x][y] == 'R':
            grid[x][y] = 'G'

copy_grid = copy.deepcopy(grid)

for rgb in RGB:
    for x in range(n):
        for y in range(n):
            if copy_grid[x][y] == rgb:
                count2 += 1
                bfs(x, y, rgb)

print(count, count2)
