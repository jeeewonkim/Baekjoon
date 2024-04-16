import sys, heapq

INF = int(1e9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

t = [0] + list(map(int, input().split()))
district = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    district[a].append([b, l])
    district[b].append([a, l])

result = []



def find(start):
    q = []
    heapq.heappush(q, [start, 0])
    res = t[start]
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i, d in district[now]:
            cost = dist + d
            if cost <= m and cost < distance[i]:
                heapq.heappush(q, [i, cost])
                if distance[i] == INF:
                    res += t[i]
                distance[i] = cost

    result.append(res)


for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    find(i)
#print(result)
print(max(result))
