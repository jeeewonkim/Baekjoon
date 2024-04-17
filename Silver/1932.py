import sys
input = sys.stdin.readline

n = int(input())
d = [[] for _ in range(n)]
for i in range(n):
    d[i] =list(map(int, input().split()))

for i in range(1,n):
    d[i][0] += d[i-1][0]
    d[i][i] += d[i-1][i-1]
    for j in range(1,i):
        d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[-1]))
    # if graph[i][leftDP[1]] < graph[i][leftDP[1]+1] :
    #     leftDP = [graph[i][leftDP[1]+1], leftDP[1]+1]
    # else:
    #     leftDP = [graph[i][leftDP[1]], leftDP[1]]
    #
    # if rightDP[i][rightDP[1]-1] < graph[i][rightDP[1]] :
    #     rightDP = [graph[i][rightDP[1]], rightDP[1]]
    # else:
    #     rightDP = [graph[i][rightDP[1-1]], rightDP[1-1]]


#     leftDP = [graph[]]
#     [max(graph[i][0], graph[i][1]) ,
#     rightDP = max(graph[i][1], graph[i][2])