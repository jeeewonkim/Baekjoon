import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] =list(map(int,input().split()))

for j in range(m):

    x1, y1, x2, y2 = map(int,input().split())
    res = sum(graph[x1-1][y1-1:y2])

    for x in range(x1,x2):
        res += sum(graph[x][y1-1:y2])

    print(res)
    #print(graph[x1-1:x2][y1-1:y2])
    #print(res)
    # for x in range(x2-x1):
    #     res = res[]
    #
    # print(res)