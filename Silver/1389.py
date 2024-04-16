import sys
from collections import deque
INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
friend = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

r = []
def bacon(start):
    global result
    q = deque()
    q.append(start)
    visited = [0] * (n + 1)
    visited[start]= True
    while q:
        now = q.popleft()
        for idx in friend[now]:
            if not visited[idx]:
                visited[idx] = visited[now]+1
                q.append(idx)
    r.append(sum(visited))



for i in range(1,n+1):
    bacon(i)

print(r.index(min(r))+1)