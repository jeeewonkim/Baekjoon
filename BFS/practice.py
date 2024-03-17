import sys
from collections import deque

sys = sys.stdin.readline
n, m = map(int, input().split())
tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))
# for _ in range(2):

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
maximum = 0
p1, p2 = 0, 0


def bfs(x, y):
    global p1,p2, maximum
    maximum = 0
    queue.append((x, y))
    tree[x][y] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #and maximum <= tree[nx][ny]
            if 0 <= nx < n and 0 <= ny < n :
                #maximum = max(tree[nx][ny], maximum)
                if maximum < tree[nx][ny]:
                    maximum = tree[nx][ny]
                    print(maximum, nx, ny)
                    queue.append((nx, ny))
                    tree[nx][ny] = 0
        p1 += maximum
        print(nx,ny)

bfs(0,2)
print(maximum)
