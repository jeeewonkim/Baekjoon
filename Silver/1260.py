import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
graph = [[False]*(n+1) for _ in range(n+1)]
for i in range(m):
    p1, p2 = map(int, input().split())
    graph[p1][p2], graph[p2][p1] = True, True

visited_d = [False] * (n + 1)
visited_b = [False] * (n + 1)
def dfs(v,visited):
    visited[v]= True
    print(v, end =  " ")
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]:
            dfs(i, visited)
def bfs(start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v , end = ' ')
        for i in range(1, n+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True




dfs(v,visited_d )
print()
bfs(v,visited_b )


