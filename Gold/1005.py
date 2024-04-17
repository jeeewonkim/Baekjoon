import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(distance,w):
    q = []
    heapq.heappush(q,(w,time[w]))
    distance[w] = time[w]

    while q:
        #print(q)
        now,dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + time[i]
            #print(distance[i])
            if (distance[i]!= INF and cost >=distance[i]) or (distance[i] == INF and cost<distance[i]):
                distance[i] = cost
                heapq.heappush(q,(i, cost))
    return distance

T = int(input())
for i in range(T):
    n, k = map(int,input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    #distance = time
    distance = [INF] *(n)
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y-1].append((x-1))
    #print(graph)
    w = int(input())
    a = dijkstra(distance,w-1)
    if w == 1: print(a[-1])
    else: print(a[0] if a[0]!=INF else time[w-1])