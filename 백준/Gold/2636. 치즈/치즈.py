import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
cheese = []
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_cheese = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))
    total_cheese += sum(graph[i])
result = 0


def find_air():
    global result
    air = deque([(0, 0)])
    cheese = deque([])
    while air:
        x, y = air.popleft()
        if graph[x][y] == 0:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                    if graph[nx][ny] == 0:
                        air.append((nx,ny))
                    elif graph[nx][ny]== 1:
                        cheese.append((nx,ny))
                    visit[nx][ny] = 1

    for x, y in cheese:
        graph[x][y] = 0

    return len(cheese)



time = 1
while True:
    visit = [[0] * (m) for _ in range(n)]
    cheese_cnt = find_air()
    total_cheese -= cheese_cnt
    if total_cheese == 0:
        print(time, cheese_cnt, end = "\n")
        break
    time +=1
