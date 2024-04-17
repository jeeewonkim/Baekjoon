import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(v1):
    q = []
    distance = [INF] * (N + 1)

    heapq.heappush(q, (0, v1))
    distance[v1] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if cost < distance[node_index]:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

start = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
# 1->v1->v2->N
path1 = start[v1] + v1_distance[v2] + v2_distance[N]
# 1->v2->v1->N
path2 = start[v2] + v2_distance[v1] + v1_distance[N]

result = min(path1, path2)

print(result if result < INF else -1)
