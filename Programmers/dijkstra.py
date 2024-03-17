import heapq

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(1, (cost, i[0]))


def solution(n, s, a, b, fares):

    for i in range(fares):
        graph[fares[i][0]].append((fares[i][1], fares[i][2]))

    dijkstra(s)
    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
    answer = 0
    return answer

n, s, a, b, fares = map(int, input().split())

solution(n,s,a,b,fares)