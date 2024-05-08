import sys
input = sys.stdin.readline

n = int(input())
graph = [[]for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
min_cost = sys.maxsize

def back(start,next, value, visited):
    global min_cost
    if len(visited) == n:
        if graph[next][start] != 0:
            min_cost = min(min_cost, value + graph[next][start])
        return
    for i in range(n):
        if graph[next][i]!=0 and i not in visited and value < min_cost:
            visited.append(i)
            back(start, i, value + graph[next][i], visited)
            visited.pop()

for i in range(n):
    back(i,i,0,[i])
print(min_cost)