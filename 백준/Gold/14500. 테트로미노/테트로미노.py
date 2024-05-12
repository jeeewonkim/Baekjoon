import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

#긴 네모 (2) 정사각형 (1) ㄹ자(4) ㅜ자(4)
dx = [[0,0,0,0],[0,1,2,3],[0,1,0,1],[0,1,1,2],[1,0,0,1],[1,2,0,1],[0,0,1,1],[0,1,2,1],[1,0,1,1],[1,0,1,2],[0,0,0,1],[0,1,2,2],[0,0,0,1],[0,0,1,2],[0,1,1,1],[0,1,2,0],[0,0,0,1],[2,0,1,2],[1,1,1,0]]
dy = [[0,1,2,3],[0,0,0,0],[0,0,1,1],[0,0,1,1],[0,1,2,1],[0,0,1,1],[0,1,1,2],[0,0,0,1],[0,1,1,2],[0,1,1,1],[0,1,2,1],[0,0,0,1],[0,1,2,0],[0,1,1,1],[0,0,1,2],[0,0,0,1],[0,1,2,2],[0,1,1,1],[0,1,2,2]]


for i in range(n):
    graph[i] = list(map(int, input().split()))
max_sum = 0

for x in range(n):
    for y in range(m):
        for i in range(len(dx)):
            sum = 0
            for j in range(4):
                nx =  x+ dx[i][j]
                ny = y+ dy[i][j]
                if 0<=nx<n and 0<=ny<m:
                    sum += graph[nx][ny]
            max_sum = max(sum, max_sum)

print(max_sum)