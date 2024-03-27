import sys
input = sys.stdin.readline

n = int(input())


graph = list(map(int,input().split()))
maxDP = graph
minDP = graph
for i in range(n-1):
    graph = list(map(int,input().split()))
    maxDP = [graph[0]+max(maxDP[0],maxDP[1]), graph[1]+max(maxDP[0],maxDP[1],maxDP[2]), graph[2]+max(maxDP[1],maxDP[2])]
    minDP =  [graph[0]+min(minDP[0],minDP[1]), graph[1]+min(minDP[0],minDP[1],minDP[2]), graph[2]+min(minDP[1],minDP[2])]

print(max(maxDP), min(minDP))

