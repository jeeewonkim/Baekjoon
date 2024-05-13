import sys, heapq
input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visit = [INF] *(n+1)
result = []
def find(x):
    q = deque()
    q.append(x)
    visit[x] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visit[i] == INF:
                visit[i] = visit[now]+1
                if(visit[i] == k):
                    result.append(i)
                q.append(i)

find(x)
result.sort()
if not result:
    print(-1)
else:
    for i in result:
        print(i)