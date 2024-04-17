import sys
from collections import deque
sys = sys.stdin.readline
INF = int(10001)

def bfs(start):
    visited = [-1] * (v + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i, d in graph[now]:
            if visited[i] == -1:
                visited[i]  += visited[now] + d+1
                queue.append(i)
    max_distance = max(visited)
    return [visited.index(max_distance), max_distance]


v = int(input())
graph = [[] for _ in range(v+1)]
for i in range(v):
    tree = list(map(int, input().split()))
    node = tree[0]
    for t in range(1,len(tree)-1,2):
        graph[node].append((tree[t], tree[t+1]))

# for i in range(1,v+1):
#     max_res = max(bfs(i), max_res)


print(bfs(bfs(1)[0])[1])
# print(floyd())


#메모리초과 플루이드
# def floyd():
#     dist = [[INF] * (v + 1) for _ in range(v + 1)]
#
#     print(dist)
#     for i in range(1, v + 1):
#         dist[i][i] = 0
#         for n,d in graph[i]:
#             dist[i][n] = d
#     for k in range(1,v+1):
#         for i in range(1,v+1):
#             for j in range(1,v+1):
#                 dist[i][j]  = min(dist[i][j],dist[i][k] + dist[k][j])
#
#     max_dist = 0
#     for i in range(1,v+1):
#         for j in range(1,v+1):
#             if dist[i][j]!=INF:
#                 max_dist = max(max_dist, dist[i][j])
#
#     return max_dist