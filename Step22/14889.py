import sys
from itertools import combinations
n = int(sys.stdin.readline().strip())
soc = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result= float('inf')

def team(L, idx):
    global result
    if L == n//2:
        start, link = 0, 0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start+=soc[i][j]
                elif not visited[i] and not visited[j]:
                    link += soc[i][j]
        result = min(result, abs(start-link))
        return
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i] = True
                team(L+1, i+1)
                visited[i] = False
                
team(0,0)
print(result)