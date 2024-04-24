from collections import deque
def solution(n, computers):
    c = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j :
                continue
            if computers[i][j] == 1:
                c[i].append(j)
                
    visited = [0] * (n)
    def search(start):
        q = deque()
        q.append(start)
        visited[start]
        while q:
            now = q.popleft()
            for n in c[now]:
                if visited[n] == 0:
                    visited[n] = 1
                    q.append(n)
    res = 0
    for i in range(n):
        if visited[i] == 0:
            res +=1
            search(i)
    return res