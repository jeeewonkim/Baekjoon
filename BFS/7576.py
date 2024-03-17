# 토마토
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomato = []
queue = deque([])
for _ in range(n):
    tomato.append(list(map(int, input().split())))
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            queue.append((y, x))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def ripen():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                queue.append((ny, nx))

result = 0
ripen()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result - 1)
