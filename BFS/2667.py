# 단지번호붙이기

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

house_count = 0
house_list = list()


def find(x, y):
    global house_count, house_list, house
    house_count = 1
    queue = deque()
    queue.append((x, y))
    house[x][y] +=1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if house[nx][ny] == 0:
                continue
            if house[nx][ny] == 1:
                house[nx][ny] = house[x][y] + 1
                queue.append((nx, ny))
                house_count += 1
    house_list.append(house_count)
    return


count = 0
for x in range(n):
    for y in range(n):
        if house[x][y] == 1:
            count += 1
            find(x, y)
house_list.sort()
print(count)
for i in range(count):
    print(house_list[i])
