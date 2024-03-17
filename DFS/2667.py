import sys
input = sys.stdin.readline

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip())))
visited = [[0] * (n+1) for _ in range(n+1)]
dx=[-1,1,0,0]
dy = [0,0,-1,1]

count = 0
def dfs(x,y):
    global count

    if x<0 or x>=n or y<0 or y>=n:
        return

    if grid[x][y] == 1:
        count +=1
        grid[x][y] = 0
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            dfs(nx,ny)


result =[]
for x in range(n):
    for y in range(n):
        if grid[x][y] == 1:
            dfs(x,y)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for r in result:
    print(r)