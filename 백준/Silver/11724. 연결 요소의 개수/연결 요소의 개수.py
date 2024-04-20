import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] *(n+1)

def search(start):
    q = deque()
    q.append(start)
    visited[start] =True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
res =0
for i in range(1, n+1):
    if visited[i] == False:
        search(i)
        res +=1
print(res)