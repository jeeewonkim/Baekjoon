import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < (dist):
            continue

        for n_index, n_cost in graph[now]:
            cost = dist + n_cost
            if distance[n_index] > cost:
                distance[n_index] = cost
                heapq.heappush(q,(cost, n_index))
    return distance



N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

result = 0
b = dijkstra(X)
for i in range(1, N + 1):
    a = dijkstra(i)
    print(a,b)
    result = max(result, a[X] + b[i])

print(result)
